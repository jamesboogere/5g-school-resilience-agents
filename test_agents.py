"""
Unit tests for specialized agents.
Tests run in offline mode (no LLM calls) to verify data flow and model integrity.
"""
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

from src.models import (
    AgentInput, AgentName, ScenarioPhase, NetworkTelemetry, NetworkStatus,
    SeverityLevel, AgentRecommendation, EscalationStatus,
)
from src.agents.network_resilience_agent import NetworkResilienceAgent
from src.agents.school_services_agent import SchoolServicesAgent
from src.agents.health_nutrition_agent import HealthNutritionAgent
from src.agents.policy_legal_agent import PolicyLegalAgent


def make_telemetry(degraded: bool = True) -> NetworkTelemetry:
    return NetworkTelemetry(
        timestamp=datetime.utcnow(),
        latency_ms=185.4 if degraded else 18.0,
        packet_loss_pct=12.3 if degraded else 0.3,
        gateway_status=NetworkStatus.DEGRADED if degraded else NetworkStatus.NOMINAL,
        bandwidth_mbps=2.1 if degraded else 52.0,
        connected_devices=87,
        sync_errors=23 if degraded else 0,
        signal_strength_dbm=-89.0 if degraded else -68.0,
    )


def make_agent_input(
    agent: AgentName,
    phase: ScenarioPhase = ScenarioPhase.NETWORK_DEGRADATION,
) -> AgentInput:
    return AgentInput(
        scenario_phase=phase,
        agent=agent,
        context={"school_name": "Test School", "student_count": 300},
        telemetry=make_telemetry(),
    )


# ---------------------------------------------------------------------------
# Model tests (no LLM)
# ---------------------------------------------------------------------------

class TestModels:
    def test_network_telemetry_valid(self):
        t = make_telemetry()
        assert t.latency_ms == 185.4
        assert t.gateway_status == NetworkStatus.DEGRADED

    def test_agent_recommendation_defaults(self):
        rec = AgentRecommendation(
            agent=AgentName.NETWORK_RESILIENCE,
            scenario_phase=ScenarioPhase.NETWORK_DEGRADATION,
            summary="Test",
            actions=["Action 1"],
            severity=SeverityLevel.HIGH,
            confidence=0.85,
        )
        assert rec.requires_human_approval is False
        assert rec.escalation_status == EscalationStatus.NONE
        assert len(rec.policy_references) == 0

    def test_agent_input_serialization(self):
        inp = make_agent_input(AgentName.NETWORK_RESILIENCE)
        data = inp.model_dump()
        assert data["scenario_phase"] == "network_degradation"
        assert data["agent"] == "5G_Network_Resilience_Agent"


# ---------------------------------------------------------------------------
# Agent prompt tests (no LLM calls)
# ---------------------------------------------------------------------------

class TestAgentPrompts:
    def test_network_agent_has_system_prompt(self):
        agent = NetworkResilienceAgent.__new__(NetworkResilienceAgent)
        assert "5G" in agent.system_prompt
        assert "latency" in agent.system_prompt.lower()

    def test_health_agent_safety_guardrail_in_prompt(self):
        agent = HealthNutritionAgent.__new__(HealthNutritionAgent)
        assert "NEVER" in agent.system_prompt
        assert "clinical diagnos" in agent.system_prompt.lower()

    def test_policy_agent_mentions_dppa(self):
        agent = PolicyLegalAgent.__new__(PolicyLegalAgent)
        assert "DPPA" in agent.system_prompt or "Data Protection" in agent.system_prompt

    def test_school_agent_mentions_offline(self):
        agent = SchoolServicesAgent.__new__(SchoolServicesAgent)
        assert "offline" in agent.system_prompt.lower()


# ---------------------------------------------------------------------------
# Response parser tests
# ---------------------------------------------------------------------------

class TestResponseParser:
    SAMPLE_RESPONSE = """
SUMMARY: Network is critically degraded with 185ms latency and 12% packet loss.
SEVERITY: high
CONFIDENCE: 0.87
REQUIRES HUMAN APPROVAL: NO

ACTIONS:
- Activate edge cache for offline learning content
- Prioritize health monitoring traffic using QoS rules
- Switch agricultural IoT to local logging mode
- Notify school IT administrator via SMS fallback

DATA GAPS:
- Root cause of 5G gateway degradation unknown
- Backup 4G/LTE availability not confirmed

REASONING:
The telemetry shows significant degradation that warrants immediate action.
"""

    def test_extract_list_section_actions(self):
        from src.agents.base_agent import BaseAgent
        actions = BaseAgent._extract_list_section(self.SAMPLE_RESPONSE, "ACTIONS")
        assert len(actions) == 4
        assert "edge cache" in actions[0].lower()

    def test_extract_list_section_data_gaps(self):
        from src.agents.base_agent import BaseAgent
        gaps = BaseAgent._extract_list_section(self.SAMPLE_RESPONSE, "DATA GAPS")
        assert len(gaps) == 2

    def test_extract_field_severity(self):
        from src.agents.base_agent import BaseAgent
        severity = BaseAgent._extract_field(self.SAMPLE_RESPONSE, "SEVERITY")
        assert severity == "high"

    def test_extract_field_confidence(self):
        from src.agents.base_agent import BaseAgent
        confidence = BaseAgent._extract_field(self.SAMPLE_RESPONSE, "CONFIDENCE")
        assert float(confidence) == 0.87

    def test_extract_requires_human(self):
        from src.agents.base_agent import BaseAgent
        val = BaseAgent._extract_field(self.SAMPLE_RESPONSE, "REQUIRES HUMAN APPROVAL")
        assert "NO" in val.upper()


# ---------------------------------------------------------------------------
# Edge Gateway tests
# ---------------------------------------------------------------------------

class TestEdgeGateway:
    def test_pseudonymization_consistent(self):
        from src.edge.gateway import EdgeGateway
        gw = EdgeGateway("KPS-004")
        p1 = gw.pseudonymize("student-001")
        p2 = gw.pseudonymize("student-001")
        assert p1 == p2
        assert p1.startswith("STU-")

    def test_different_students_different_pseudonyms(self):
        from src.edge.gateway import EdgeGateway
        gw = EdgeGateway("KPS-004")
        p1 = gw.pseudonymize("student-001")
        p2 = gw.pseudonymize("student-002")
        assert p1 != p2

    def test_sensor_validation_valid_record(self):
        from src.edge.gateway import EdgeGateway
        gw = EdgeGateway("KPS-004")
        valid, errors = gw.validate_sensor_record({
            "sensor_id": "SOIL-001",
            "timestamp": "2026-11-03T10:00:00Z",
            "reading_type": "soil_moisture",
            "value": 18.5,
        })
        assert valid is True
        assert len(errors) == 0

    def test_sensor_validation_missing_field(self):
        from src.edge.gateway import EdgeGateway
        gw = EdgeGateway("KPS-004")
        valid, errors = gw.validate_sensor_record({
            "sensor_id": "SOIL-001",
            "value": 18.5,
        })
        assert valid is False
        assert len(errors) > 0

    def test_sync_queue(self):
        from src.edge.gateway import EdgeGateway
        gw = EdgeGateway("KPS-004")
        rid = gw.queue_for_sync({"student_id": "STU-ABC", "data": "test"})
        assert rid is not None
        assert gw.get_cache_status()["sync_queue_depth"] == 1


# ---------------------------------------------------------------------------
# Audit Logger tests
# ---------------------------------------------------------------------------

class TestAuditLogger:
    def test_load_empty_log(self, tmp_path):
        from src.audit_logger import AuditLogger
        logger = AuditLogger(tmp_path / "test.jsonl")
        entries = logger.load_all_entries()
        assert entries == []

    def test_log_and_reload(self, tmp_path):
        from src.audit_logger import AuditLogger
        logger = AuditLogger(tmp_path / "audit.jsonl")
        rec = AgentRecommendation(
            agent=AgentName.NETWORK_RESILIENCE,
            scenario_phase=ScenarioPhase.NETWORK_DEGRADATION,
            summary="Test recommendation",
            actions=["Action A"],
            severity=SeverityLevel.MEDIUM,
            confidence=0.75,
        )
        entry_id = logger.log_agent_recommendation("session-001", rec)
        entries = logger.load_all_entries()
        assert len(entries) == 1
        assert entries[0]["entry_id"] == entry_id
