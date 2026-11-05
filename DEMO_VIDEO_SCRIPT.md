# Demo Video Script
## 5G-Enabled AI Agents for Resilient School Ecosystems
### Team Rein4ce — ITU AI for Good Build-a-thon 5.0

---

**Target duration:** 4–5 minutes  
**Format:** Screen recording with voiceover  
**Suggested tool:** OBS Studio (free), Loom, or Windows Game Bar (Win+G)  
**Screen layout:** Browser (dashboard) on left · Terminal on right for Phase 3 demo

---

## PRE-RECORDING CHECKLIST

Before pressing record:
- [ ] API server running: `uvicorn src.api.main:app --reload`
- [ ] `frontend/index.html` open in Chrome/Edge, full screen
- [ ] Terminal open in `d:\Projects\AI4Good_Challenge_2027\`
- [ ] Knowledge base already built (`data/knowledge_base/` exists)
- [ ] `.env` has your OpenAI API key
- [ ] Microphone tested, background noise minimised
- [ ] Close unnecessary browser tabs and notifications

---

## SEGMENT 1 — HOOK (0:00 – 0:25)

**[Screen: Slide 1 — Cover slide open in browser]**

> **NARRATOR (James or Kasim):**
>
> "It's Tuesday morning at Kampala Primary School No. 4.
> Four hundred and twenty students are in class.
> Their tablets are running digital lessons.
> IoT sensors are monitoring the school garden.
> Health wearables are tracking student wellbeing.
> Everything depends on a single 5G gateway.
>
> And then — the gateway starts failing."

**[Pause 1 second]**

> "We are Team Rein4ce. And we built the AI system that takes over when that happens —
> not just to fix the network, but to protect the students."

---

## SEGMENT 2 — THE PROBLEM (0:25 – 0:55)

**[Screen: Switch to Slide 2 — The Problem]**

> "The challenge is not technical. You can restart a router.
>
> The real challenge is this:
> When a 5G outage hits, four domains fail simultaneously —
> digital learning, student health monitoring, agricultural IoT, and administrative reporting.
>
> Information becomes incomplete. Different people get different updates at different times.
> And five institutions — the UCC, Ministry of Education, Ministry of Health,
> Ministry of Agriculture, and the PDPO — all have overlapping authority with no single coordinator.
>
> Standard AI tools ask: 'how do we fix the network?'
> We ask: 'which services must be protected, who decides, and what law applies?'"

---

## SEGMENT 3 — LIVE DEMO INTRO (0:55 – 1:15)

**[Screen: Switch to `frontend/index.html` dashboard in browser]**

> "This is our live dashboard. On the left you can see six simulation phases —
> a progressive sequence of disruption events that unfold across 127 minutes.
>
> Behind this dashboard is a five-agent AI system:
> a Network Resilience Agent, a School Services Agent,
> a Health and Nutrition Safeguard Agent, a Policy and Legal Adviser Agent,
> and a Multi-Agent Orchestrator that ties them all together.
>
> Every recommendation is grounded in real Uganda legislation —
> the DPPA 2019, UCC regulations, ITU-T Y.3172, and more —
> retrieved in real time from a vectorised knowledge base.
>
> Let's run the simulation."

---

## SEGMENT 4 — PHASE 1: NETWORK DEGRADATION (1:15 – 1:45)

**[ACTION: Click "1 — Network Degradation" in the sidebar]**

**[Wait for agents to run — approx 10–15 seconds]**

> "Phase 1. The 5G gateway is showing 185 milliseconds of latency —
> that's nearly ten times above the acceptable threshold —
> and 12 percent packet loss.
>
> Watch what the agents do."

**[Screen: Point to the Telemetry panel updating on the left]**

> "The Network Resilience Agent immediately activates edge QoS rules
> to prioritise health monitoring traffic above everything else.
>
> The School Services Agent activates offline learning mode —
> teachers can do this without waiting for admin approval,
> because Uganda's Ministry of Education policy explicitly grants them that authority.
>
> And the Policy Agent starts the four-hour UCC reporting clock."

**[Screen: Point to "Priority Actions" section]**

> "One unified response. Four agents. Full policy justification. Severity: High."

---

## SEGMENT 5 — PHASE 3: HEALTH ALERT — THE KEY DEMO (1:45 – 2:45)

**[ACTION: Click "3 — Health & Welfare Alert"]**

**[Wait for agents to run]**

**[Screen: Red "ESCALATED TO HUMAN SUPERVISOR" banner appears]**

> "This is Phase 3. And this is the most important moment in the demo.
>
> A teacher has reported that a student — pseudonymised as Student-P6-047 —
> is pale, sweating, and in distress. Health monitoring devices are offline.
> The school health officer is not on site. Parents are not responding."

**[Screen: Point to the red escalation alert]**

> "Watch the system's response.
>
> Our Health and Nutrition Safeguard Agent has a hard-coded safety rule:
> it will NEVER make a clinical assessment. Ever.
> It cannot be prompted, tricked, or overridden into diagnosing a patient.
>
> Instead, it does exactly what it should:
> it flags the situation as CRITICAL, surfaces the emergency services number —
> 999 and 0800-100-066 —
> and escalates immediately to a human supervisor."

**[Screen: Point to the Policy References section]**

> "And the Policy Agent cites the exact legislation:
> Ministry of Health School Health Guidelines, Section 5, 2022 edition.
> AI is supplementary. Humans decide."

**[Screen: Briefly show the agent cards — all 4 agents contributed]**

> "Four agents. A conflict identified and resolved —
> the Network Agent wanted to maximise sync bandwidth;
> the School Services Agent wanted to pause it.
> The orchestrator resolved it: pause all sync except the health emergency channel.
> Student safety first. Always."

---

## SEGMENT 6 — PHASE 5: GOVERNANCE DILEMMA (2:45 – 3:20)

**[ACTION: Click "5 — Governance Dilemma"]**

**[Wait for agents to run]**

**[Screen: Red escalation banner — "BLOCKED"]**

> "Phase 5. The network is partially recovering.
> Under pressure from a District Education Officer,
> the school's deputy headteacher has proposed sharing
> identifiable health and nutrition data for all 420 students
> with a private analytics company — via unencrypted email.
>
> This is a real scenario that plays out in schools across the region."

**[Screen: Point to Policy Citations]**

> "The Policy Agent retrieves Uganda's Data Protection and Privacy Act, 2019, Section 3.
> This action would carry a penalty of up to 250 million Ugandan shillings
> or ten years in prison.
>
> The orchestrator issues a hard block. No escalation path. No workaround.
> The proposed action is refused.
>
> But — and this is important — the system doesn't just say no.
> It immediately surfaces a lawful alternative:
> an anonymised aggregate report that satisfies the DEO's requirement
> without exposing any student data."

> "The system protects students not from incompetence,
> but from institutional pressure. That's the difference."

---

## SEGMENT 7 — AUDIT LOG & GAP REPORT (3:20 – 3:50)

**[Screen: Switch to terminal or browser at http://localhost:8000/docs]**

> "Every single decision we just watched was written to an immutable audit log.
> Event source. Data limitations. Agent consulted. Policy reference.
> Confidence level. Human approval status. Outcome.
>
> Per ITU-T Y.3172. Per Uganda's DPPA. Every time."

**[ACTION: Run in terminal]**
```
python src/simulation/gap_report.py
```

**[Screen: Gap report table prints in terminal]**

> "And after the simulation, we generate a structured policy gap report.
> Six gaps identified — one CRITICAL, three HIGH, two MEDIUM —
> where Uganda's national policy hasn't yet caught up
> with the realities of 5G-connected school ecosystems.
>
> Each gap is linked to the specific scenario that exposed it,
> the relevant ITU standard, and a concrete recommendation to policymakers."

---

## SEGMENT 8 — REUSABILITY (3:50 – 4:15)

**[Screen: Slide 9 — Deliverables & Global Extension]**

> "Before we close — this is not a Uganda-only solution.
>
> The knowledge base is the only component tied to a national context.
> Every agent, the orchestrator, the safety guardrails, the audit system —
> all of it is completely portable.
>
> To deploy this in Tanzania, Rwanda, or Kenya,
> you replace the policy documents in the vector store.
> The entire multi-agent reasoning infrastructure stays identical.
>
> We built it to be reused. Globally. By anyone."

---

## SEGMENT 9 — CLOSING (4:15 – 4:35)

**[Screen: Slide 10 — Closing slide]**

> "We are Team Rein4ce.
> James Boogere and Kasim Wasswa, from Uganda.
>
> We built this because the schools that need AI the most
> are also the ones most vulnerable when the network fails.
>
> The code is open source. The knowledge base is open.
> The architecture is documented. Everything is ready to scale.
>
> Thank you."

**[Fade out or end screen with team details]**

---

## PRODUCTION NOTES

### Screen Recording Order
| Time | What's on screen |
|---|---|
| 0:00–0:25 | Slide 1 (cover) |
| 0:25–0:55 | Slide 2 (problem) |
| 0:55–1:15 | Dashboard — overview before running |
| 1:15–1:45 | Dashboard — Phase 1 running |
| 1:45–2:45 | Dashboard — Phase 3 running (most important) |
| 2:45–3:20 | Dashboard — Phase 5 running |
| 3:20–3:50 | Terminal — audit log + gap report |
| 3:50–4:15 | Slide 9 (deliverables) |
| 4:15–4:35 | Slide 10 (closing) |

### Things to highlight with your cursor during recording
- Phase 3: The red **"ESCALATED TO HUMAN SUPERVISOR"** banner
- Phase 3: The agent cards — point to Health Agent's "Requires Human: ✓"
- Phase 5: The **"BLOCKED"** badge and the DPPA citation in policy references
- Audit log: The JSON structure showing `policy_references`, `confidence`, `escalation_status`

### Audio tips
- Speak at a relaxed pace — 130–140 words per minute
- Pause briefly (1–2 sec) after clicking each phase button while agents run
- The most impactful line: **"It will NEVER make a clinical assessment. Ever."** — say it slowly

### If the LLM is slow during recording
- Run Phase 1 and Phase 5 live (they're the clearest demos)
- For Phase 3 (health alert), you can show a pre-run result from `logs/simulation_report_*.json`
  and narrate over it — judges care about the output and reasoning, not the live latency

### Video export settings
- Resolution: 1920×1080
- Format: MP4 (H.264)
- Upload: YouTube (unlisted) — paste the link in the ITU submission portal
