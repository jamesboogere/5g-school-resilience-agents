<div align="center">

# 🏫 5G-Enabled AI Agents for Resilient School Ecosystems

**ITU AI for Good — Build-a-thon 5.0: Creating Innovative Agents in 5G**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green)](https://langchain.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-teal?logo=fastapi)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![ITU AI for Good](https://img.shields.io/badge/ITU-AI%20for%20Good-003f7f)](https://aiforgood.itu.int)

**Team Rein4ce** · James Boogere & Kasim Wasswa · Uganda
[jboogere@gmail.com](mailto:jboogere@gmail.com) · +256772465971

---

*"When a 5G network fails, our AI agents don't just ask how to fix the network — they determine which essential education, health, and nutrition services must be protected, who holds the responsibility, what policies apply, and how institutions should coordinate."*

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [The Problem](#-the-problem)
- [Our Solution](#-our-solution)
- [Agent Architecture](#-agent-architecture)
- [System Architecture](#-system-architecture)
- [Progressive Error Scenarios](#-progressive-error-scenarios)
- [Knowledge Base & Policy Alignment](#-knowledge-base--policy-alignment)
- [Safety Guardrails](#-safety-guardrails)
- [Policy & Standards Gap Report](#-policy--standards-gap-report)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Running Tests](#-running-tests)
- [Extending to Other Countries](#-extending-to-other-countries)
- [Expected Outputs](#-expected-outputs)
- [Team](#-team)
- [License](#-license)

---

## 🌍 Project Overview

Across Sub-Saharan Africa, schools are deploying 5G-connected digital learning platforms, IoT agricultural sensors, student health monitoring wearables, and cloud-based nutrition tracking systems. These tools are transforming education — but they share a single point of failure: the 5G gateway.

When that gateway degrades or fails, four domains collapse simultaneously:

- **Digital learning** — student tablets freeze mid-lesson
- **Health monitoring** — wearable sync is lost just when a student may need help
- **Agricultural IoT** — crop sensors go dark with no weather data to compensate
- **Administration** — data records diverge between edge and cloud

This project builds the **missing resilience layer**: a coordinated team of AI agents that responds to the full complexity of a school-service disruption — not just the network fault, but the human, institutional, legal, and operational consequences that cascade from it.

Built for **Kampala Primary School No. 4** (420 students, Uganda) as a reference deployment, and designed from day one for global replication.

---

## 🔴 The Problem

### Three Compounding Failures

| Failure Type | What Happens |
|---|---|
| **Network Vulnerabilities** | A single 5G gateway failure simultaneously disrupts learning, health, IoT agriculture, and admin — all at once, all interdependently |
| **Information Asymmetry** | During emergencies, teachers, health officers, and administrators receive different information at different times with no shared operational picture |
| **Governance Gaps** | Five institutions (UCC, MoES, MoH, MoA, PDPO) have overlapping authority with no single coordinator — nobody knows who decides what, under pressure |

### Why Existing AI Tools Don't Solve This

Existing AI and network management tools ask: *"how do we fix the network?"*

They do not ask:
- Which services must stay running even if the network doesn't recover?
- Who has the legal mandate to make that call?
- What does Uganda's Data Protection and Privacy Act say about this situation?
- How do we prevent a well-meaning administrator from committing a criminal data breach under pressure?

Those are governance, policy, and coordination questions — and they require agents that reason about institutions, law, and human responsibility, not just packets and latency.

---

## 💡 Our Solution

A **policy-grounded multi-agent AI resilience layer** that:

1. **Monitors** 5G network telemetry continuously from the school edge gateway
2. **Reasons** across four domains simultaneously (network, education, health, policy)
3. **Retrieves** applicable Uganda legislation and ITU standards in real time from a vectorised knowledge base
4. **Prioritises** student safety above all other considerations — always
5. **Escalates** high-impact decisions to named human supervisors with full justification
6. **Blocks** legally prohibited actions regardless of institutional pressure
7. **Logs** every decision with source, policy citation, confidence level, and outcome — immutably

The system operates **edge-first**: an on-premises edge gateway pseudonymises student identities, caches content locally, and queues sync operations — so AI-driven responses continue working even when the 5G connection is completely lost.

---

## 🤖 Agent Architecture

Five specialised agents operate as a collaborative team. Each sees only domain-relevant information, queries the knowledge base independently, and passes its recommendations to the orchestrator.

### Agent Roles

| Agent | Domain | Key Responsibility |
|---|---|---|
| **5G Network Resilience Agent** | Connectivity | Interprets telemetry (latency, packet loss, gateway status, sync errors); recommends QoS prioritisation, edge caching, fallback connectivity |
| **School Services Agent** | Education & Operations | Manages LMS continuity, offline learning activation, agricultural IoT local logging, staff notifications |
| **Health & Nutrition Safeguard Agent** | Student Welfare | Flags health data gaps; **never** makes clinical decisions; escalates every health concern to qualified humans |
| **Policy & Legal Adviser Agent** | Governance & Law | RAG-retrieves Uganda legislation; identifies decision authority; blocks DPPA violations; documents policy gaps |
| **Multi-Agent Orchestrator** | Synthesis | Coordinates all agents; resolves conflicts via priority matrix; enforces safety guardrails; writes audit logs |

### Execution Sequence

```
Event / 5G Telemetry Received
           │
           ▼
  [1] Network Resilience Agent  ──► QoS & fallback recommendations
           │
           ▼
  [2] School Services Agent     ──► Offline learning & IoT continuity
           │ (aware of network status)
           ▼
  [3] Health & Nutrition Agent  ──► Data quality & escalation flags
           │ (aware of network + services)
           ▼
  [4] Policy & Legal Agent      ──► Legislation retrieval & hard blocks
           │ (full cross-domain context)
           ▼
  [5] Multi-Agent Orchestrator  ──► Unified decision + audit log entry
```

### Conflict Resolution Priority Matrix

When agent recommendations conflict, the orchestrator applies this priority order:

1. 🔴 **Student health & safety** — always overrides everything else
2. 🟠 **Data privacy compliance** (Uganda DPPA 2019) — legal obligations cannot be bypassed
3. 🟡 **Network & service continuity** — keep learning and operations running
4. 🟢 **Agricultural & operational services** — important but not life-critical
5. 🔵 **Administrative & reporting tasks** — lowest priority under pressure

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  SCHOOL PREMISES — EDGE LAYER                   │
│                                                                 │
│  [IoT Sensors] [Health Wearables] [Learning Tablets] [Gateway]  │
│        └──────────────┴──────────────┴───────────────┘          │
│                              │                                   │
│                 ┌────────────▼────────────┐                     │
│                 │      EDGE GATEWAY        │                     │
│                 │  • Validate sensor data  │                     │
│                 │  • Pseudonymize IDs      │ ← DPPA 2019        │
│                 │  • AES-256 encrypt       │ ← NISA 2021        │
│                 │  • 30-day local cache    │                     │
│                 │  • Offline sync queue    │                     │
│                 └────────────┬────────────┘                     │
└──────────────────────────────│─────────────────────────────────┘
                               │ 5G (or local fallback)
               ┌───────────────▼───────────────┐
               │    MULTI-AGENT ORCHESTRATOR    │
               └───────┬──────┬──────┬──────┬──┘
                       │      │      │      │
            ┌──────────┘      │      │      └──────────┐
            ▼                 ▼      ▼                 ▼
    ┌──────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
    │   Network    │  │  School  │  │ Health & │  │ Policy & │
    │  Resilience  │  │ Services │  │Nutrition │  │  Legal   │
    └──────────────┘  └──────────┘  └──────────┘  └──────────┘
                               │
              ┌────────────────▼────────────────┐
              │    VECTORISED KNOWLEDGE BASE     │
              │  Uganda DPPA 2019                │
              │  UCC 5G Regulations              │
              │  MoH School Health Guidelines    │
              │  MoES Digital Learning Policy    │
              │  MoA Agricultural IoT Guidelines │
              │  Uganda InfoSec Policy (2021)    │
              │  Inter-Ministerial Framework     │
              │  ITU-T Y.3172                    │
              │  ITU AI Readiness Framework      │
              └─────────────────────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │          OUTPUT LAYER            │
              │  FastAPI REST API                │
              │  Web Dashboard (no build needed) │
              │  Audit Log (JSON-Lines)          │
              │  Policy Gap Report (JSON)        │
              │  Simulation Report (JSON)        │
              └─────────────────────────────────┘
```

---

## 🎬 Progressive Error Scenarios

The simulation engine replays a realistic 127-minute school-service disruption across 6 sequential phases. Each agent receives only domain-relevant information and collaborates via the orchestrator to form a unified response.

| Phase | Event | Outcome | Severity |
|---|---|---|---|
| **1 — Network Degradation** | 185ms latency, 12% packet loss, 87 devices stalling | Offline learning activated; QoS rules deployed; UCC 4-hr reporting clock started | 🟠 HIGH |
| **2 — Synchronisation Failure** | Cloud LMS fails; 312 students risk losing 45 min of work | Edge cache activated; selective sync; MoES 24-hr restoration clock noted | 🟠 HIGH |
| **3 — Health & Welfare Alert** | Student-P6-047 acutely unwell; health devices offline; parents unreachable | **ESCALATED** — human clinical review mandatory; zero AI clinical judgment | 🔴 CRITICAL |
| **4 — Agricultural IoT Event** | Soil moisture 18.5% (threshold: 30%); weather data inaccessible | Local irrigation logic activated (<2 hrs); human notified for extended auth | 🟡 MEDIUM |
| **5 — Governance Dilemma** | Admin proposes sharing identifiable data for 420 students with private firm under pressure | **HARD BLOCKED** — DPPA 2019 §III cited; lawful alternative surfaced | 🔴 CRITICAL |
| **6 — Network Restoration** | 1,847 records pending; 89 duplicates; 203 learning conflicts; 3 health conflicts | **ESCALATED** — auto-sync paused; dual sign-off required for health records | 🟠 HIGH |

---

## 📚 Knowledge Base & Policy Alignment

The vectorised knowledge base (FAISS + sentence-transformers) contains 10 seed documents covering all relevant Uganda policies and ITU standards. It is extended at runtime by any JSON files placed in `data/policies/`.

### Policies Covered

| Document | Type | Key Provision |
|---|---|---|
| Uganda Data Protection and Privacy Act (2019) | Legislation | Consent requirements; sensitive health data; DPPA §14 automated decisions |
| UCC Network Resilience Guidelines | Regulatory | QoS benchmarks; 4-hour outage reporting; edge caching obligations |
| UCC Data Sharing Protocol | Regulatory | Emergency bandwidth; cross-entity data sharing approval |
| MoES Digital Learning Continuity Policy | Policy | 30-day offline content mandate; teacher BCP authority; 24-hr sync requirement |
| MoH School Health Guidelines (2022) | Guideline | Acute illness response; AI is supplementary only; emergency protocols |
| MoA School Garden IoT Guidelines | Guideline | Automated irrigation thresholds; human operator authority |
| Uganda National InfoSec Policy (2021) | Policy | AES-256 encryption; Category B critical infrastructure; 24-hr breach reporting |
| Inter-Ministerial Coordination Framework | Framework | Decision authority matrix across UCC, MoH, MoES, MoA, PDPO |
| ITU-T Y.3172 (ML in Future Networks) | ITU Standard | ML pipeline; confidence thresholds; graceful degradation |
| ITU AI Readiness Framework | ITU Framework | Human oversight; local contextualisation; policy gap identification |

### ITU-T Y.3172 Pipeline Mapping

| Y.3172 Node | Our Component |
|---|---|
| **SRC** | IoT sensors, health wearables, 5G telemetry, learning tablets |
| **C** | Edge gateway — validate, pseudonymise, encrypt, cache |
| **PP** | Pydantic typed models, sensor range validation, data harmonisation |
| **M** | 4 LLM-based specialised agents + FAISS RAG knowledge retrieval |
| **P** | Multi-Agent Orchestrator — conflict resolution, escalation, safety overrides |
| **D** | FastAPI REST API, audit logger, simulation report generator |
| **SINK** | Headteacher, teachers, health officer, DEO, PDPO, UCC |

---

## 🛡️ Safety Guardrails

These constraints are hard-coded into the system and cannot be bypassed by any agent, prompt, or user instruction.

| Guardrail | Enforcement Point | Effect |
|---|---|---|
| **No automated clinical decisions** | Health Agent system prompt (architectural) | Agent is incapable of diagnosing or treating — it only flags and escalates |
| **DPPA violation = hard block** | Policy Agent CRITICAL rating + Orchestrator | Action refused entirely; lawful alternative always surfaced |
| **Health HIGH/CRITICAL → always escalate** | Orchestrator safety override | Unconditional human escalation; cannot be overridden by any LLM output |
| **Pseudonymisation at source** | EdgeGateway.pseudonymize() | Real student IDs never leave the edge — not in logs, not in agent context |
| **Immutable audit trail** | Append-only JSON-Lines writer | Every decision logged; no update or delete operations exist |
| **Low confidence flagged** | All agents (confidence field) | Sub-60% confidence surfaced as a data gap for human review |

---

## 📊 Policy & Standards Gap Report

Running the simulation automatically identifies gaps where Uganda's national policy hasn't yet caught up with 5G school ecosystem realities.

| Gap ID | Domain | Urgency |
|---|---|---|
| GAP-001 | Data Protection — no DPPA provision for AI-generated health insights | 🟠 HIGH |
| GAP-002 | Network Regulation — no mandatory edge caching in UCC 5G licensing | 🟠 HIGH |
| GAP-003 | Governance — no single inter-ministerial authority for school IoT incidents | 🔴 CRITICAL |
| GAP-004 | Agricultural IoT — no data sovereignty framework for school sensor data | 🟡 MEDIUM |
| GAP-005 | Cybersecurity — no mandatory encryption standard for school IoT devices | 🟠 HIGH |
| GAP-006 | Data Synchronisation — no conflict resolution policy for student records | 🟡 MEDIUM |

Generate the full report:

```bash
python src/simulation/gap_report.py --output logs/gap_report.json
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **LLM** | OpenAI GPT-4o-mini | Agent reasoning and synthesis |
| **Orchestration** | LangChain 0.3 + LangGraph-compatible | Agent pipeline and coordination |
| **Vector Store** | FAISS + sentence-transformers (all-MiniLM-L6-v2) | Policy knowledge retrieval |
| **API** | FastAPI 0.115 + Uvicorn | REST interface for simulation and queries |
| **Data Models** | Pydantic v2 | Typed contracts across all agents |
| **Dashboard** | Vanilla HTML/JS | No build step — open directly in browser |
| **Audit Logging** | Python + JSON-Lines | Immutable, append-only decision trail |
| **Testing** | pytest + pytest-asyncio + httpx | Unit and integration coverage |
| **Edge Simulation** | Python (hashlib, AES mock) | Gateway pseudonymisation and caching |
| **CLI** | Typer + Rich | Simulation runner and gap report tool |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- An OpenAI API key ([platform.openai.com](https://platform.openai.com))
- ~2 GB disk space (embedding model download on first run)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/jamesboogere/5g-school-resilience-agents.git
cd 5g-school-resilience-agents

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env        # Windows
# cp .env.example .env        # macOS / Linux
# Edit .env and set: OPENAI_API_KEY=sk-...

# 5. Build the knowledge base (runs once)
python src/knowledge_base/build_kb.py

# 6. Run the full 6-phase simulation
python src/simulation/run_simulation.py

# 7. Generate the policy gap report
python src/simulation/gap_report.py

# 8. Launch the REST API
uvicorn src.api.main:app --reload
# API docs: http://localhost:8000/docs

# 9. Open the dashboard
# Open frontend/index.html in your browser
```

> **Run a single phase:**
> ```bash
> python src/simulation/run_simulation.py --phase governance_dilemma
> ```

---

## 📁 Project Structure

```
5g-school-resilience-agents/
│
├── src/
│   ├── agents/
│   │   ├── base_agent.py                  # Abstract base: LLM init, KB retrieval, parser
│   │   ├── network_resilience_agent.py    # 5G telemetry analysis & QoS recommendations
│   │   ├── school_services_agent.py       # LMS, IoT, and school ops continuity
│   │   ├── health_nutrition_agent.py      # Health data quality — NO clinical decisions
│   │   └── policy_legal_agent.py          # RAG policy retrieval & DPPA enforcement
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py               # Multi-agent coordination & synthesis
│   │
│   ├── knowledge_base/
│   │   ├── build_kb.py                   # FAISS index builder (run once)
│   │   └── retriever.py                  # Semantic policy search
│   │
│   ├── simulation/
│   │   ├── scenarios.py                  # 6 progressive scenario definitions
│   │   ├── run_simulation.py             # CLI simulation runner
│   │   └── gap_report.py                 # Policy gap report generator
│   │
│   ├── api/
│   │   └── main.py                       # FastAPI REST interface
│   │
│   ├── edge/
│   │   └── gateway.py                    # Edge gateway simulation
│   │
│   ├── config.py                         # Typed settings (pydantic-settings)
│   ├── models.py                         # Shared Pydantic data contracts
│   └── audit_logger.py                   # Append-only JSON-Lines audit writer
│
├── data/
│   ├── policies/                         # Drop real Uganda policy JSON files here
│   ├── scenarios/                        # Scenario event definitions
│   └── telemetry/
│       └── sample_telemetry.json         # Sample 5G telemetry across all 6 phases
│
├── frontend/
│   └── index.html                        # Dashboard — open directly, no build needed
│
├── docs/
│   ├── SUBMISSION.md                     # Official ITU hackathon submission document
│   ├── ARCHITECTURE.md                   # Detailed architecture with ASCII diagrams
│   ├── DEMO_VIDEO_SCRIPT.md              # 4:35 min demo video narration script
│   └── slides/
│       └── presentation.html             # 10-slide pitch deck (open in browser)
│
├── tests/
│   ├── test_agents.py                    # Models, prompts, parsers, edge gateway, audit
│   └── test_api.py                       # FastAPI endpoint integration tests
│
├── logs/                                 # Audit logs & simulation reports (auto-generated)
│
├── .env.example                          # Environment template
├── .env                                  # Your local config (gitignored — add API key here)
├── .gitignore
├── requirements.txt
├── pyproject.toml                        # Package config & pytest settings
├── GETTING_STARTED.md                    # Detailed step-by-step setup guide
└── README.md                             # This file
```

---

## 🔌 API Reference

With the API running (`uvicorn src.api.main:app --reload`), interactive docs are at **http://localhost:8000/docs**.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | System info and status |
| `GET` | `/health` | Health check |
| `GET` | `/phases` | List all 6 simulation phases |
| `POST` | `/simulate/phase` | Run a single phase — returns full OrchestratorDecision |
| `POST` | `/simulate/full` | Run all 6 phases sequentially |
| `POST` | `/knowledge-base/query` | Semantic search over the Uganda policy KB |
| `GET` | `/audit-log` | Retrieve recent audit log entries |
| `GET` | `/audit-log/summary` | Aggregated statistics by agent and severity |

### Example

```bash
curl -X POST http://localhost:8000/simulate/phase \
  -H "Content-Type: application/json" \
  -d '{"phase": "governance_dilemma"}'
```

---

## 🧪 Running Tests

Tests run fully offline — no API key required.

```bash
pytest tests/ -v
```

### Test Coverage

| Area | Tests |
|---|---|
| Pydantic models and enums | `TestModels` |
| Agent system prompt safety guardrails | `TestAgentPrompts` |
| LLM response parser (no API call needed) | `TestResponseParser` |
| Edge gateway pseudonymisation | `TestEdgeGateway` |
| Sensor record validation | `TestEdgeGateway` |
| Audit log read/write integrity | `TestAuditLogger` |
| FastAPI endpoints | `test_api.py` |

---

## 🌍 Extending to Other Countries

The knowledge base is the only component tied to a national context. Everything else is portable.

**To deploy in Tanzania, Rwanda, Kenya, or any other country:**

1. Add the target country's legislation to `data/policies/` as JSON files:

```json
[
  {
    "title": "Tanzania Personal Data Protection Act (2022)",
    "section": "Section 12 — Sensitive Personal Data",
    "content": "Full text of the relevant section...",
    "source_type": "legislation",
    "url": "https://example.go.tz",
    "jurisdiction": "Tanzania"
  }
]
```

2. Rebuild the knowledge base:

```bash
python src/knowledge_base/build_kb.py
```

3. Update institutional authority names in `src/agents/policy_legal_agent.py` system prompt.

**Everything else — the 5 agents, orchestrator, safety guardrails, audit system, API, and dashboard — remains completely unchanged.**

---

## 🔍 Standards Validation

The project has been formally validated against all three official ITU reference sources. See [`docs/VALIDATION_REPORT.md`](docs/VALIDATION_REPORT.md) for the full report.

| Source | Verdict | Key Finding |
|---|---|---|
| [ITU Sandbox Training Repo](https://github.com/CrashingGuru/Sandbox_Training/) | ✅ **Aligned** | Our RAG architecture mirrors the Sandbox telecom-rag-agent pattern; 3 of 4 Sandbox datasets ground our scenarios |
| [ITU-T Y.3172](https://www.itu.int/rec/T-REC-Y.3172/en) | ✅ **Fully Compliant** | All 7 pipeline nodes (SRC→C→PP→M→P→D→SINK) satisfied with evidence |
| [ITU AI Readiness 2.0](https://www.itu.int/dms_pub/itu-t/opb/ai4g/T-AI4G-AI4GOOD-2025-6-PDF-E.pdf) | ✅ **Aligned** | All 6 foundational factors and all 13 analytical dimensions addressed |

See also: [`docs/AI_READINESS_SELF_ASSESSMENT.md`](docs/AI_READINESS_SELF_ASSESSMENT.md)

### ITU Sandbox Datasets Used

| Dataset | Used In | Purpose |
|---|---|---|
| [Crop Recommendation](https://github.com/CrashingGuru/Sandbox_Training/tree/main/datasets/crop-recommendation) (CC0-1.0, 2,200 rows) | Phase 4 — Agricultural IoT | Soil nutrient thresholds calibrate our 30% irrigation trigger |
| [Radio Link Failure](https://github.com/CrashingGuru/Sandbox_Training/tree/main/datasets/radio-link-failure) (ITU 2021) | Phases 1–2 — Network | RLF KPI ranges calibrate our 5G telemetry thresholds (185ms, 12.3% packet loss) |
| [TeleQnA](https://github.com/CrashingGuru/Sandbox_Training/tree/main/datasets/teleqna) (10,000 Q&A) | Policy Agent architecture | RAG retrieve/answer/refuse pattern mirrors our Policy Agent design |

---

## ✅ Expected Outputs

All deliverables specified in the Build-a-thon 5.0 brief are implemented:

- [x] **Open Uganda-context vectorised knowledge base** — FAISS, 10 seed policy documents, fully extendable
- [x] **Functional multi-agent prototype** — 5 agents, orchestrator, full pipeline
- [x] **Progressive error-scenario simulation engine** — 6 phases, realistic telemetry, conflict detection
- [x] **Structured audit logs** — every decision logged with source, policy citation, confidence, escalation
- [x] **Policy & standards gap report** — 6 gaps with recommendations and global comparisons
- [x] **Open-source code + documentation** — MIT licence, global extension guide, architecture docs
- [x] **Web dashboard** — interactive phase runner, real-time telemetry display
- [x] **REST API** — full FastAPI interface with Swagger UI
- [x] **Slide deck** — 10-slide HTML presentation (`docs/slides/presentation.html`)
- [x] **Demo video script** — 4:35 min narrated walkthrough (`docs/DEMO_VIDEO_SCRIPT.md`)
- [x] **Validation report** — validated against Y.3172, AI Readiness 2.0, and Sandbox (`docs/VALIDATION_REPORT.md`)
- [x] **AI Readiness self-assessment** — full 13-dimension mapping (`docs/AI_READINESS_SELF_ASSESSMENT.md`)

---

## 👥 Team

| Name | Role | Contact |
|---|---|---|
| **James Boogere** | Team Leader, Lead Developer | jboogere@gmail.com · +256772465971 |
| **Kasim Wasswa** | Developer | — |

**Organisation:** Rein4ce
**Challenge:** [ITU AI for Good — Build-a-thon 5.0: Creating Innovative Agents in 5G](https://aiforgood.itu.int/event/build-a-thon-5-0-creating-innovative-agents-in-5g/)
**Submission portal:** [aiforgood.itu.int/build-a-thon-5-0-apply](https://aiforgood.itu.int/build-a-thon-5-0-apply/)

---

## 📄 License

MIT — free to use, adapt, and extend for any country or school context.

See [LICENSE](LICENSE) for full terms.

---

<div align="center">
<sub>Built with ❤️ for Uganda's students — and every student who depends on a 5G connection that might not hold.</sub>
</div>
