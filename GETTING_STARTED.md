# Getting Started
## 5G-Enabled AI Agents for Resilient School Ecosystems
### Team Rein4ce — ITU AI for Good Build-a-thon 5.0

---

## Prerequisites

- Python **3.10+**
- An **OpenAI API key** (gpt-4o-mini is the default — cost-efficient for demos)
- ~2 GB disk space (for sentence-transformer embedding model download)
- Internet connection for first setup (embedding model download + LLM calls)

---

## Step 1 — Clone & Install

```bash
# Clone the repository
git clone https://github.com/rein4ce-learning/5g-school-resilience-agents.git
cd 5g-school-resilience-agents

# Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

---

## Step 2 — Configure Environment

```bash
# Copy the example env file
copy .env.example .env      # Windows
cp .env.example .env        # macOS/Linux

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-...
```

> **Note:** The `.env` file is in `.gitignore` and will never be committed.

---

## Step 3 — Build the Knowledge Base

This builds the Uganda-context vectorized policy knowledge base using FAISS.
It runs once; after that it's cached locally.

```bash
python src/knowledge_base/build_kb.py
```

Expected output:
```
🔨 Building Uganda-context vectorized knowledge base...
⚠️  No policy documents found. Generating seed knowledge base...
  ✂️  Split into 42 chunks.
  🧠 Generating embeddings (this may take a moment)...
  ✅ Knowledge base saved to: data/knowledge_base
  📊 Total vectors: 42
```

> The seed knowledge base includes 10 Uganda policy documents covering DPPA 2019,
> UCC regulations, MoH guidelines, MoES policy, MoA IoT guidelines, ITU-T Y.3172,
> and the ITU AI Readiness Framework. Add real PDF/JSON documents to `data/policies/`
> to extend it.

---

## Step 4 — Run the Simulation

Run all 6 progressive school disruption phases:

```bash
python src/simulation/run_simulation.py
```

Or run a single phase:

```bash
python src/simulation/run_simulation.py --phase health_welfare_alert
python src/simulation/run_simulation.py --phase governance_dilemma
```

The simulation will:
- Execute all 4 agents sequentially per phase
- Print colour-coded decisions with severity levels
- Show human escalation alerts for critical situations
- Save a full JSON report to `logs/simulation_report_<id>.json`
- Append all decisions to `logs/audit.jsonl`

---

## Step 5 — Generate the Policy Gap Report

```bash
python src/simulation/gap_report.py
```

With audit log enrichment (run after simulation):

```bash
python src/simulation/gap_report.py --from-log logs/audit.jsonl --output logs/gap_report.json
```

---

## Step 6 — Launch the API

```bash
uvicorn src.api.main:app --reload
```

The API will be available at: **http://localhost:8000**

Interactive API docs (Swagger UI): **http://localhost:8000/docs**

### Key Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | System info |
| `GET` | `/health` | Health check |
| `GET` | `/phases` | List all 6 scenario phases |
| `POST` | `/simulate/phase` | Run a single phase |
| `POST` | `/simulate/full` | Run all 6 phases |
| `POST` | `/knowledge-base/query` | Semantic policy search |
| `GET` | `/audit-log` | View audit log entries |
| `GET` | `/audit-log/summary` | Aggregated audit statistics |

### Example API call

```bash
curl -X POST http://localhost:8000/simulate/phase \
  -H "Content-Type: application/json" \
  -d '{"phase": "governance_dilemma"}'
```

---

## Step 7 — Open the Dashboard

With the API running, open `frontend/index.html` in your browser.

> On Windows: right-click `frontend/index.html` → Open with Chrome/Edge

The dashboard lets you:
- Run any of the 6 scenario phases interactively
- See real-time 5G telemetry metrics
- View per-agent recommendations and orchestrator decisions
- Track escalation alerts and policy citations
- Follow the session timeline

---

## Step 8 — Run Tests

```bash
pytest tests/ -v
```

Tests cover:
- All Pydantic models and enums
- Agent system prompt safety guardrails
- LLM response parser (no API key needed)
- Edge gateway pseudonymization and sensor validation
- Audit logger read/write integrity

---

## Project Structure

```
AI4Good_Challenge_2027/
├── src/
│   ├── agents/              # 4 specialized AI agents + base class
│   ├── orchestrator/        # Multi-agent coordination & synthesis
│   ├── knowledge_base/      # FAISS vector store builder & retriever
│   ├── simulation/          # 6-phase scenario engine & gap report
│   ├── api/                 # FastAPI REST interface
│   ├── edge/                # Edge gateway simulation
│   ├── config.py            # Typed settings (pydantic-settings)
│   ├── models.py            # Shared data contracts
│   └── audit_logger.py      # Append-only audit log writer
├── data/
│   ├── policies/            # Drop real Uganda policy JSON/PDFs here
│   ├── scenarios/           # Scenario definitions
│   └── telemetry/           # Sample 5G telemetry data
├── frontend/
│   └── index.html           # Web dashboard (no build step)
├── docs/
│   ├── SUBMISSION.md        # Official hackathon submission document
│   └── ARCHITECTURE.md      # System architecture & design
├── tests/                   # Unit & integration tests
├── logs/                    # Audit logs & simulation reports (auto-generated)
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Package config & pytest settings
└── GETTING_STARTED.md       # This file
```

---

## Extending the Knowledge Base

To add real policy documents, create JSON files in `data/policies/` with this format:

```json
[
  {
    "title": "Uganda Communications Commission — 5G Spectrum Policy",
    "section": "Section 3 — School Connectivity Requirements",
    "content": "Full text of the relevant section...",
    "source_type": "regulatory",
    "url": "https://www.ucc.co.ug/policy",
    "jurisdiction": "Uganda"
  }
]
```

Then rebuild the knowledge base:

```bash
python src/knowledge_base/build_kb.py
```

---

## Team

**Rein4ce** | ITU AI for Good — Build-a-thon 5.0  
James Boogere — jboogere@gmail.com | +256772465971  
Kasim Wasswa
