# System Architecture
## 5G-Enabled AI Agents for Resilient School Ecosystems

---

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│              SCHOOL PREMISES — EDGE LAYER                            │
│                                                                      │
│  [IoT Sensors]  [Health Wearables]  [Learning Tablets]  [5G Gateway]│
│       │               │                    │                 │       │
│       └───────────────┴────────────────────┴─────────────────┘       │
│                                    │                                  │
│                       ┌────────────▼────────────┐                    │
│                       │   EDGE GATEWAY           │                    │
│                       │  • Validate sensor data  │                    │
│                       │  • Pseudonymize IDs      │                    │
│                       │    (DPPA 2019 compliant) │                    │
│                       │  • AES-256 encryption    │                    │
│                       │  • Local content cache   │                    │
│                       │    (30-day buffer)       │                    │
│                       │  • Offline sync queue    │                    │
│                       └────────────┬────────────┘                    │
└────────────────────────────────────│────────────────────────────────┘
                                     │ 5G (or cached local events)
                    ┌────────────────▼────────────────┐
                    │     MULTI-AGENT ORCHESTRATOR     │
                    │                                  │
                    │  Priority Matrix:                │
                    │  1. Student health & safety      │
                    │  2. Data privacy (DPPA 2019)     │
                    │  3. Network & service continuity │
                    │  4. Agricultural / operational   │
                    │  5. Administrative & reporting   │
                    │                                  │
                    │  → Resolves conflicts            │
                    │  → Enforces safety guardrails    │
                    │  → Escalates to human supervisor │
                    │  → Writes immutable audit log    │
                    └──────┬──────┬──────┬──────┬─────┘
                           │      │      │      │
              ┌────────────┘      │      │      └──────────────┐
              ▼                   ▼      ▼                     ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │   Network    │  │    School    │  │  Health &    │  │  Policy &    │
    │  Resilience  │  │   Services   │  │  Nutrition   │  │    Legal     │
    │    Agent     │  │    Agent     │  │  Safeguard   │  │   Adviser    │
    │              │  │              │  │    Agent     │  │    Agent     │
    │ 5G telemetry │  │ LMS offline  │  │ Data quality │  │ RAG retrieval│
    │ QoS routing  │  │ Ag IoT cache │  │ Privacy check│  │ Policy cite  │
    │ Fallback conn│  │ Sync mgmt    │  │ NO clinical  │  │ Gap analysis │
    └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
              │              │                  │                  │
              └──────────────┴──────────────────┴──────────────────┘
                                       │
                         ┌─────────────▼──────────────┐
                         │  VECTORIZED KNOWLEDGE BASE  │
                         │         (FAISS)             │
                         │                             │
                         │  Uganda DPPA 2019           │
                         │  UCC 5G Regulations         │
                         │  MoH School Health (2022)   │
                         │  MoES Digital Learning      │
                         │  MoA Agricultural IoT       │
                         │  NITA-U InfoSec Policy      │
                         │  Inter-Ministerial Framework│
                         │  ITU-T Y.3172               │
                         │  ITU AI Readiness Framework │
                         └─────────────────────────────┘
                                       │
                    ┌──────────────────▼──────────────────┐
                    │          OUTPUT LAYER                │
                    │                                      │
                    │  FastAPI REST  │  Web Dashboard      │
                    │  Audit Log     │  Gap Report JSON    │
                    │  (JSON-Lines)  │  Simulation Report  │
                    └──────────────────────────────────────┘
```

---

### Agent Execution Sequence

```
Event/Telemetry Received
        │
        ▼
[1] Network Resilience Agent
    → Analyzes 5G telemetry
    → Recommends QoS / fallback
        │
        ▼
[2] School Services Agent
    → Aware of network status from [1]
    → Recommends offline/continuity actions
        │
        ▼
[3] Health & Nutrition Safeguard Agent
    → Aware of network + service state
    → Flags health data gaps, never diagnoses
        │
        ▼
[4] Policy & Legal Adviser Agent
    → Has full cross-domain context
    → Retrieves policies, blocks violations
        │
        ▼
[5] Multi-Agent Orchestrator (Synthesis)
    → Combines all 4 recommendations
    → Resolves conflicts by priority matrix
    → Applies safety overrides
    → Determines human escalation
    → Writes audit log entry
    → Returns OrchestratorDecision
```

---

### ITU-T Y.3172 Pipeline Mapping

| Y.3172 Node | Component |
|---|---|
| **SRC** | IoT sensors, health wearables, 5G telemetry, LMS |
| **C** | Edge gateway (validate, pseudonymize, encrypt, cache) |
| **PP** | Pydantic typed models, sensor range validation |
| **M** | 4 specialized LLM agents + FAISS RAG |
| **P** | Multi-Agent Orchestrator (conflict resolution + escalation) |
| **D** | FastAPI + audit logger + simulation report |
| **SINK** | Headteacher, teachers, health officer, DEO, PDPO, UCC |

---

### Safety Guardrails

| Guardrail | Where Enforced |
|---|---|
| No automated clinical decisions | Hard-coded in Health Agent system prompt |
| DPPA violation = hard block | Policy Agent returns CRITICAL + Orchestrator blocks |
| Health HIGH/CRITICAL → human escalation | Orchestrator safety override (cannot be bypassed) |
| Low confidence (<60%) flagged | All agents include confidence field and data gaps |
| Audit immutability | Append-only JSON-Lines — no update/delete operations |
| Pseudonymization at source | EdgeGateway.pseudonymize() before any transmission |

---

### Data Flow (Privacy-by-Design)

```
Student ID "S-001"
      │
      ▼ EdgeGateway.pseudonymize()
"STU-4F2A8C1E0B3D"  ← only this leaves the edge
      │
      ▼ AES-256 encryption
[ENCRYPTED PAYLOAD]
      │
      ▼ Cloud / Agents
Never sees real student ID
```

Real ID ↔ pseudonym mapping: **stored only on edge device, never transmitted.**
