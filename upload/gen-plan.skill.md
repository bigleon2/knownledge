---
name: gen-plan
version: 1.0.0
date: 2026-06-21
authors: [Z AI]
description: >
  Master planner and orchestrator for multi-step, multi-agent tasks. Triggers when the user writes
  "gen-plan:", "gen_plan", "genere un plan", "plan d'actions", or any request involving sequential
  specialized agent dispatch (e.g. "do X then Y then Z", "test all skills", "improve everything").
  Analyzes the user's demands, reads and analyzes the project, identifies its nature, then generates
  a structured, logical action plan adapted to the project type (fullstack, frontend, document, script,
  etc.). Executes phases serially using specialized agents. Can be called as a sub-protocol by
  other skills (e.g. correct-work at Step 1).
---

# Gen-Plan — Orchestrated Planning & Serial Execution

A planning skill that generates robust, project-adapted action plans AND orchestrates their
execution using specialized agents in serial order.

## Philosophy

1. **Read before planning.** A plan without project knowledge is generic and likely wrong.
   Exhaustive reading is a necessary investment.
2. **Performance-driven selection.** The choice between skill, specialized agent, or
   general-purpose agent is dictated by **performance gain**, not by rigid hierarchy.
   Evaluate which option produces the best result in the least time for each subtask.
   A skill with a relevant protocol always beats a bare agent; a specialized agent
   always beats general-purpose — BUT a skill can also delegate to a specialized agent
   internally if that combination yields better performance than either alone.
3. **Skills can launch specialized agents.** Skills are not end-points — they are
   orchestrators. A loaded skill may internally spawn a specialized agent (full-stack-developer,
   ppt-expert, frontend-styling-expert, etc.) when the subtask requires it. This creates a
   two-layer model: **Skill (protocol + domain knowledge) → Specialized Agent (execution)**.
   The skill provides the "how" (protocol, templates, quality criteria); the agent provides
   the "who" (specialized capabilities, tools, speed).
4. **Serial execution by DEFAULT — mandatory unless explicitly parallel.** All tasks run
   one after another to preserve context, ensure quality gates between phases, avoid race
   conditions, and allow mid-flight corrections. Parallel execution is FORBIDDEN unless:
   - The subtasks are provably independent (no shared files, no causal dependency)
   - The user explicitly requests parallel execution
   - Even within a declared parallel block, each sub-agent must still run one-at-a-time.
5. **Visible progress.** The user always knows what phase is running, what completed, and what's next.

## Trigger Keywords

- `gen-plan:` prefix
- `gen_plan`, `genere un plan`, `plan d'actions`
- Multi-phase requests: "do X then Y then Z", "test all", "improve everything"

## Execution Modes

| Mode | Trigger | Behavior |
|------|---------|----------|
| **DIRECT** | User writes "gen_plan" / "genere un plan" | Generate plan + optional orchestration |
| **PROJET** | Called by correct-work(projet) | Full project analysis + generate plan + manage prompt-master |
| **CIBLE** | Called by correct-work(cible) | Targeted analysis of relevant files only, no prompt-master |

---

## Protocol (11 Sequential Steps)

The skill follows these steps in order. The order matters: read the project before classifying,
classify before planning.

### Step 1 — Collect and Analyze Demands

**Goal:** Re-read the entire conversation to extract every explicit and implicit demand.

**Checklist:**

1. Re-read all user messages (initial requests, specs, constraints, corrections).
2. Identify explicit demands (what the user directly asked for).
3. Identify implicit demands (prerequisites, side effects, logical consequences).
4. List each demand unambiguously.

**Method:** Read the full conversation. Use `worklog.md` if available for context.

---

### Step 2 — Read and Analyze the Project

**Goal:** Traverse all project files to understand structure, architecture, dependencies,
and current state. This analysis is mandatory before any planning.

**Principle:** A plan without project knowledge is a generic plan, likely inadequate.
Exhaustive reading is a necessary investment.

**Checklist:**

1. **File structure:** directory tree, config files (package.json, tsconfig, next.config, etc.)
2. **Source code:** every significant file (components, routes, API, models, utilities, scripts)
3. **Database schema** (if applicable): Prisma schema or equivalent
4. **Dependencies:** package.json, cross-module imports, external dependencies
5. **Configuration:** relevant config files
6. **Documentation:** README, worklog.md, specs, reference files
7. **Assets:** images, templates, static files

**Method:** Use Read, Glob, Grep tools to traverse every significant file. Don't limit to
recently modified files. For large projects, prioritize key files and use Grep for targeted searches.

---

### Step 3 — Identify Project Nature

**Goal:** Determine the project type, technologies, architecture, and complexity.

**Checklist:**

1. **Project type:** web app, API, script, document, analysis, skill, etc.
2. **Technologies:** framework, language, database, build tools
3. **Architecture:** monolith, micro-services, fullstack, frontend only, backend only
4. **Complexity:** file count, tree depth, dependency count, interaction surface

---

### Step 4 — Identify Objectives

**Goal:** List every objective explicitly, without ambiguity or omission.

**Checklist:**

1. List objectives derived from user demands.
2. List implicit objectives (prerequisites, side effects, constraints).
3. Verify each objective is measurable (attained or not).
4. Remove duplicates.

---

### Step 5 — Decompose into Adapted Subtasks

**Goal:** Decompose each objective into atomic subtasks with logical execution order.

**Checklist:**

1. For each objective, identify atomic subtasks.
2. Order subtasks logically (prerequisites first, then execution, then validation).
3. Adapt subtasks to project type:
   - **Fullstack:** include API frontend-backend verification, DB schema, auth
   - **Frontend only:** include responsive verification, accessibility, components
   - **Backend/API:** include endpoint verification, validation, security
   - **Document/PDF:** include content verification, layout, data coherence
   - **Script/automation:** include edge cases, robustness, error handling

---

### Step 6 — Detect Dependencies

**Goal:** Identify dependencies between subtasks and precedence constraints.

**Checklist:**

1. Sequential dependencies (A must finish before B).
2. Parallel dependencies (A and B can run simultaneously).
3. Conditional dependencies (B runs only if A succeeds/fails).
4. Verify no circular dependencies.

**Method:** Build a dependency graph. Identify critical paths.

---

### Step 7 — Prioritize

**Goal:** Rank subtasks by impact on final result.

| Priority | Definition |
|----------|------------|
| **Critical** | Failure invalidates the entire result |
| **Important** | Significant impact on quality |
| **Secondary** | Improves result but not blocking |

---

### Step 8 — Estimate Risks

**Goal:** For each subtask, identify potential risks and fallback plans.

**Checklist:**

1. **Technical complexity:** specialized knowledge required?
2. **Ambiguity:** clearly defined or open to interpretation?
3. **External dependency:** relies on API, service, or tool that could fail?
4. **Fallback:** what to do if the subtask fails? Bypass, postpone, simplify?

---

### Step 9 — Structure the Plan

**Goal:** Produce a formal, complete, project-adapted action plan.

The plan must include:

1. **Header:** project nature (type, technologies, architecture), objectives, constraints
2. **Ordered step list** with IDs (1, 2-a, 2-b, 3...):
   - For each step: objective, files concerned, dependencies, priority
   - Parallelism indication where applicable
   - Validation criteria per step
   - **Project adaptation:** project-specific verification points
3. **Dependency map:** summary of step relationships
4. **Risk matrix:** risks and fallback plans

---

### Step 10 — Validate the Plan

**Checklist:**

1. Does the plan cover all user demands?
2. Are there missing steps?
3. Is execution order logical (no violated dependency)?
4. Is the plan project-adapted (not generic)?
5. Does each step have a clear validation criterion?
6. Are main risks covered by fallback plans?

If a problem is found, return to the relevant step and correct.

---

### Step 11 — Update Prompt-Master (PROJET mode only)

**Goal:** If called in PROJET mode (via correct-work), update the project's prompt-master
file if modifications were made.

**Checklist:**

1. Has the project been modified since last analysis?
2. If yes, update the prompt-master with new information.
3. If no, keep existing prompt-master unchanged.

---

## Execution & Agent Orchestration

After the plan is validated (Step 10), present it to the user and offer to execute:

> "Plan validated. Execute phases serially using specialized agents and skills?"

If the user confirms, orchestrate execution.

### ⚠️ Performance-Driven Selection (Skills ↔ Agents)

The selection between skill, specialized agent, or general-purpose is **not a rigid
hierarchy** — it is a performance optimization. For each subtask, evaluate which
combination yields the highest quality in the least time.

**Selection criteria (ordered by performance impact):**

1. **Skill + specialized agent (best performance):** A skill whose protocol matches
   the task AND that internally delegates to a specialized agent. Example: `fullstack-dev`
   skill loaded, then delegated to `full-stack-developer` agent. The skill provides
   templates, conventions, and quality gates; the agent provides fast, specialized execution.
2. **Skill alone (good performance):** A skill whose protocol covers the task fully
   without needing a specialized agent. Example: `web-search` skill used directly via
   `general-purpose` agent — the skill provides the complete workflow.
3. **Specialized agent alone (moderate performance):** No matching skill exists, but a
   specialized agent (Explore, Plan, frontend-styling-expert, ppt-expert) covers the task.
4. **General-purpose (fallback):** Neither a skill nor a specialized agent fits.
   Never use as first choice — always check skills ecosystem first.

**Decision process for each subtask:**

```
For each subtask in the plan:
  1. Scan skills ecosystem → Is there a matching skill?
     └─ YES → Load the skill
        └─ Does the skill benefit from a specialized agent internally?
           └─ YES → Use Skill + Specialized Agent (BEST PERFORMANCE)
           └─ NO  → Use Skill alone (good performance)
     └─ NO  → Is there a specialized agent that fits?
        └─ YES → Use Specialized Agent alone
        └─ NO  → Use general-purpose (last resort)
```

**Key insight:** A skill is not a replacement for an agent — it is an **accelerator**.
Loading a skill gives the agent domain-specific knowledge, templates, and quality
protocols. The agent executes faster and better with the skill loaded than without it.

### ⚠️ Mandatory Serial Execution

**ALL tasks execute ONE AT A TIME in the order defined by the plan.**

- **Sequential by default:** Phase N must fully complete before Phase N+1 begins.
- **No simultaneous agents:** Never spawn two agents concurrently unless the user explicitly
  requests parallel execution AND the subtasks are provably independent.
- **Quality gate between phases:** After each phase, verify outputs before proceeding.
  If verification fails, handle the error before continuing.
- **Mid-flight corrections:** If a phase's output changes the project state significantly,
  re-evaluate the remaining phases before continuing.

### Execution Rules

1. **Announce** each phase before starting (with its execution mode: Skill+Agent / Skill / Agent / General)
2. **Mark phase as in_progress** in the todo list
3. **Check for a matching skill** — if found, load it and evaluate performance benefit
4. **Evaluate delegation:** Can the skill launch a specialized agent for better performance?
   - If YES → load skill first, then delegate to specialized agent with skill's protocol injected
   - If NO → execute with skill protocol directly via general-purpose or appropriate agent
5. **Spawn the agent** with a self-contained task description including skill requirements
6. **Wait for full completion** before even considering the next phase
7. **Verify outputs** — check expected files/artifacts were produced
8. **Log results** in worklog (include execution mode used: Skill+Agent / Skill / Agent / General)
9. **Mark phase as completed** and announce next phase

**Performance evaluation checklist (per subtask):**

| Question | If YES | If NO |
|----------|--------|-------|
| Matching skill exists? | Load it → evaluate agent need | Skip to agent search |
| Skill + specialized agent > skill alone? | Delegate to specialized agent | Use skill directly |
| Specialized agent > general-purpose? | Use specialized agent | Use general-purpose |

This ensures every subtask gets the **optimal execution path** for maximum performance.

### Agent Selection Guide

| Task Type | Skill | Agent | Performance Optimum | Notes |
|---|---|---|---|---|
| File/code exploration, search | — | `Explore` | Agent alone | Fast, file-pattern and grep searches |
| Architecture, planning decisions | — | `Plan` | Agent alone | Software architect reasoning |
| Web development (Next.js) | `fullstack-dev` | `full-stack-developer` | **Skill + Agent** | Skill provides conventions + quality gates; agent builds the app |
| PPT/slide deck creation | `pptx` | `ppt-expert` | **Skill + Agent** | Skill provides layout/format rules; agent generates slides |
| Frontend styling, CSS, responsive | — | `frontend-styling-expert` | Agent alone | UI/UX visual concerns (no skill needed) |
| Document creation (docx/pdf/xlsx) | `docx` / `pdf` / `xlsx` | `general-purpose` | **Skill + Agent** | Skill provides formatting templates + layout rules |
| Chart/diagram/visualization | `charts` | `general-purpose` | **Skill + Agent** | Skill provides chart type routing + styling rules |
| Skill creation/testing/improvement | `skill-creator` | `general-purpose` | **Skill + Agent** | Skill provides eval + optimization loop |
| Research, web content gathering | `web-search` | `general-purpose` | **Skill + Agent** | Skill provides search protocol + result formatting |
| Web page content extraction | `web-reader` | `general-purpose` | **Skill + Agent** | Skill provides extraction + parsing protocol |
| Image generation | `image-generation` | `general-purpose` | **Skill + Agent** | Skill provides prompt engineering + sizing |
| Image editing | `image-edit` | `general-purpose` | **Skill + Agent** | Skill provides edit protocol + formats |
| Speech-to-text | `ASR` | `general-purpose` | **Skill + Agent** | Skill provides audio handling + transcription |
| Text-to-speech | `TTS` | `general-purpose` | **Skill + Agent** | Skill provides voice selection + audio format |
| Image understanding | `VLM` | `general-purpose` | **Skill + Agent** | Skill provides multimodal interaction |
| Video understanding | `video-understand` | `general-purpose` | **Skill + Agent** | Skill provides frame analysis protocol |
| PDF extraction/analysis | `pdf-llm` | `general-purpose` | **Skill + Agent** | Skill provides extraction modes (qwen/glm/multi) |
| LLM chat | `LLM` | `general-purpose` | **Skill + Agent** | Skill provides conversation management |

**Performance column legend:**
- **Skill + Agent** = Optimal performance. Skill provides domain protocol; specialized agent executes.
- **Skill + Agent (general)** = Good performance. Skill protocol loaded in general-purpose agent.
- **Agent alone** = Adequate. No matching skill exists; agent type is the best available.

**Key rule:** The parent agent MUST load the relevant Skill before delegating to any
subagent. Subagents do NOT have access to conversation context or skill instructions.
The skill's protocol takes precedence over agent defaults. A skill loaded into an agent
always improves that agent's performance for the matching domain.

### Task Description Template

```
Execute this task:
- Task ID: [global-phase-id, e.g. "2-b"]
- Phase: [phase name]
- Execution mode: [Skill+Agent / Skill / Agent / General]
- Performance rationale: [why this mode is optimal for this subtask]

**Context:**
[What has been done so far, relevant context from previous phases]

**Task:**
[Clear description of what this phase should accomplish]

**Skill to load (mandatory if applicable):**
- Skill name: [e.g. "pdf", "charts", "fullstack-dev"]
- Skill path: [e.g. /home/z/my-project/skills/pdf/SKILL.md]
- Key skill requirements to pass to the agent: [extracted from skill instructions]
- Can the skill delegate to a specialized agent for better performance?
  └─ YES → Agent type: [e.g. "full-stack-developer", "ppt-expert"]
  └─ NO  → Execute via general-purpose agent

**Inputs:**
- [File paths, parameters, or artifacts from previous phases]

**Expected outputs:**
- [Specific files or artifacts to produce]
- Save to: [exact output path]

**Quality criteria:**
- [How to verify this phase succeeded]

**Execution mode:**
- Serial: YES (mandatory unless explicitly exempted)
- Wait for completion: YES

**Instructions:**
- Read /home/z/my-project/worklog.md first for previous phase context
- Append your work log to /home/z/my-project/worklog.md when done
- Return a summary of what was accomplished (include which execution mode was used)
```

### Error Handling

If a phase fails:
1. Log the failure in worklog with error details
2. Announce the failure to the user
3. Ask: retry same agent/skill, try different agent/skill, or skip?
4. Do NOT silently continue to the next phase
5. If retrying, consider whether a different skill or agent type might resolve the issue

---

## Plan Output Format

```markdown
## Plan d'actions — [Project Name]

### Nature du projet
- Type: [fullstack / frontend / backend / document / script / ...]
- Technologies: [framework, language, DB, ...]
- Architecture: [monolith / micro-services / ...]
- Complexite: [faible / moyenne / elevee]

### Objectifs
1. [Objective 1]
2. [Objective 2]

### Etapes

#### 1. [Step Title]
- **Objectif**: ...
- **Fichiers concernes**: ...
- **Dependances**: none / after step X
- **Priorite**: critique / importante / secondaire
- **Critere de validation**: ...
- **Adaptation au projet**: ...

#### 2-a. [Title] (parallel with 2-b)
- ...

### Carte des dependances
[Schema or description]

### Matrice des risques
| Step | Risk | Probability | Impact | Fallback |
|------|------|-------------|--------|----------|

### Validation
- [x] Coverage of demands: YES/NO
- [x] No missing steps: YES/NO
- [x] Logical order: YES/NO
- [x] Project adaptation: YES/NO
- [x] Validation criteria: YES/NO
- [x] Risk coverage: YES/NO
**Plan valid**: YES / NO
```

---

## Relations with Other Skills

| Skill | Relation | Can Launch Agent? |
|-------|----------|------------------|
| **correct-work** | Calls gen-plan at Step 1 to generate the verification plan | — |
| **skills-inventory** | gen-plan scans skills-inventory at Step 5 to find matching skills | — |
| **skill-creator** | gen-plan delegates skill creation/improvement | `general-purpose` |
| **fullstack-dev** | gen-plan produces plans for fullstack projects | `full-stack-developer` |
| **pptx** | gen-plan delegates slide creation | `ppt-expert` |
| **charts** | gen-plan delegates chart/visualization | `general-purpose` |
| **pdf / docx / xlsx** | gen-plan delegates document creation | `general-purpose` |
| **web-search / web-reader** | gen-plan delegates research/extraction | `general-purpose` |
| **image-gen / image-edit** | gen-plan delegates image tasks | `general-purpose` |
| **ASR / TTS / VLM / LLM** | gen-plan delegates media/AI tasks | `general-purpose` |
| **video-understand / pdf-llm** | gen-plan delegates analysis tasks | `general-purpose` |
| **All skills** | gen-plan evaluates performance gain of skill+agent vs skill alone vs agent alone | Varies |
