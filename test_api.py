"""
Integration tests for the FastAPI application.
"""
import pytest
from unittest.mock import patch, MagicMock
from httpx import AsyncClient

from src.api.main import app
from src.models import ScenarioPhase, SeverityLevel, EscalationStatus


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "Build-a-thon" in data["challenge"]


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_list_phases():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/phases")
    assert response.status_code == 200
    data = response.json()
    assert len(data["phases"]) == 6


@pytest.mark.asyncio
async def test_kb_query_no_kb():
    """Knowledge base query should return 503 if KB is not built."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/knowledge-base/query",
            json={"query": "Uganda data protection school", "k": 3},
        )
    # Either 200 (KB exists) or 503 (KB not built)
    assert response.status_code in (200, 503)


@pytest.mark.asyncio
async def test_audit_log_empty():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/audit-log")
    assert response.status_code == 200
    data = response.json()
    assert "entries" in data
