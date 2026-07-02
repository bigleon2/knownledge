# Agent Types Reference

Detailed capability matrix for all available agent types in the Task tool.
This reference supports **performance-driven selection** — see gen-plan/SKILL.md for the
full selection protocol.

## Performance Principle

**Skills are accelerators, not replacements.** Loading a skill into any agent gives that agent
domain-specific knowledge, templates, and quality protocols — improving speed and quality.
The optimal execution path is always: **Skill (protocol) + Specialized Agent (execution)**.

When no skill matches the task, a specialized agent alone still outperforms general-purpose.
General-purpose is the last resort, never the default.

## Available Agents

### `general-purpose`
- **Tools:** All tools (Read, Write, Edit, Bash, Grep, Glob, LS, Task)
- **Best for:** Multi-step research, complex file operations, multi-step tasks where no specialist fits
- **Limits:** No special domain knowledge; slower than specialists for narrow tasks
- **Performance boost:** SIGNIFICANT when a skill is loaded (skill provides domain protocol)
- **Use when:** The task spans multiple domains or requires flexible reasoning

### `Explore`
- **Tools:** All tools
- **Best for:** Fast codebase exploration, file pattern matching, keyword searches
- **Speed:** Quick (designed for rapid file/code searches)
- **Thoroughness levels:** "quick", "medium", "very thorough"
- **Performance boost:** None needed — already optimal for search tasks
- **Use when:** You need to find files, search code, understand codebase structure

### `Plan`
- **Tools:** All tools
- **Best for:** Architecture decisions, implementation strategy, identifying critical files
- **Performance boost:** None needed — already optimal for planning tasks
- **Use when:** Designing implementation plans before coding

### `frontend-styling-expert`
- **Tools:** All tools
- **Best for:** CSS, styling frameworks, responsive design, UI/UX implementation, animations, layout systems
- **Performance boost:** None needed — already specialized for visual tasks
- **Use when:** Visual/presentational aspects of web development

### `full-stack-developer`
- **Tools:** All tools, builds production-ready Next.js apps
- **Best for:** Complete websites, dashboards, web applications, real-time interfaces
- **Stack:** Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Prisma ORM
- **Performance boost:** SIGNIFICANT when `fullstack-dev` skill is loaded (conventions + quality gates)
- **Use when:** Building interactive web pages, management systems, Next.js apps

### `ppt-expert`
- **Tools:** All tools
- **Best for:** Professional slide presentations as standalone HTML files
- **Performance boost:** SIGNIFICANT when `pptx` skill is loaded (layout + format rules)
- **Use when:** Creating PPT/slide decks

## Selection Decision Tree (Performance-Driven)

```
STEP 1: Is there a matching SKILL in the ecosystem?
  └─ YES → Load the Skill
    └─ Does loading the skill + delegating to a SPECIALIZED agent
        yield better PERFORMANCE than skill alone?
      └─ YES → Skill + Specialized Agent (OPTIMAL)
      └─ NO  → Skill alone via general-purpose (GOOD)
  └─ NO → Continue to agent selection

STEP 2: Which SPECIALIZED agent fits best (no skill available)?
  Is this a Next.js web app with interactive UI?
    └─ YES → full-stack-developer
    └─ NO
      Is this a PPT/slide deck?
        └─ YES → ppt-expert
        └─ NO
          Is this purely visual/styling (CSS, responsive, animation)?
            └─ YES → frontend-styling-expert
            └─ NO
              Is this architecture/planning only (no code output)?
                └─ YES → Plan
                └─ NO
                  Is this a quick file/code search?
                    └─ YES → Explore
                    └─ NO → general-purpose (LAST RESORT)
```

**Key:** Performance is the decision driver at EVERY branch.

## Skills → Agent Mapping Reference (Performance-Driven)

| Skill Name | When to Load | Best Agent | Performance Rationale |
|---|---|---|---|
| `pdf` | PDF creation/editing | `general-purpose` | Skill provides templates + layout rules → agent executes |
| `docx` | Word document creation | `general-purpose` | Skill provides formatting + styles → agent executes |
| `xlsx` | Excel/spreadsheet creation | `general-purpose` | Skill provides data structures + chart rules → agent executes |
| `pptx` | Presentation creation | **`ppt-expert`** | Skill provides layout/format rules + expert agent for slides = OPTIMAL |
| `charts` | Charts, diagrams, visualizations | `general-purpose` | Skill provides chart type routing + styling → agent executes |
| `fullstack-dev` | Next.js web development | **`full-stack-developer`** | Skill provides conventions + quality gates + expert agent = OPTIMAL |
| `web-search` | Web research, real-time info | `general-purpose` | Skill provides search protocol + result formatting → agent executes |
| `web-reader` | Web page content extraction | `general-purpose` | Skill provides extraction + parsing protocol → agent executes |
| `image-generation` | AI image creation | `general-purpose` | Skill provides prompt engineering + sizing rules → agent executes |
| `image-edit` | AI image modification | `general-purpose` | Skill provides edit protocol + format handling → agent executes |
| `ASR` | Speech-to-text | `general-purpose` | Skill provides audio handling + transcription protocol → agent executes |
| `TTS` | Text-to-speech | `general-purpose` | Skill provides voice selection + audio format → agent executes |
| `VLM` | Image understanding/analysis | `general-purpose` | Skill provides multimodal interaction protocol → agent executes |
| `LLM` | Chat/AI conversation | `general-purpose` | Skill provides conversation management + context → agent executes |
| `video-understand` | Video content analysis | `general-purpose` | Skill provides frame analysis + temporal protocol → agent executes |
| `pdf-llm` | PDF extraction to Markdown | `general-purpose` | Skill provides extraction modes + normalization → agent executes |
| `skill-creator` | Skill creation/testing | `general-purpose` | Skill provides eval loop + optimization → agent executes |

**Note:** When a skill's best agent is marked **bold**, it means the skill can launch
that specialized agent internally for maximum performance. The skill acts as the
orchestrator (protocol) and the agent acts as the executor (specialized execution).

## Two-Layer Delegation Model

```
PARENT AGENT (gen-plan orchestrator)
│
├─ Load Skill (protocol + domain knowledge)
│   │
│   ├─ Can the skill launch a specialized agent for better performance?
│   │   ├─ YES → Delegate to SPECIALIZED AGENT (e.g. full-stack-developer, ppt-expert)
│   │   │         Skill provides: protocol, templates, quality criteria
│   │   │         Agent provides: specialized execution, domain expertise, speed
│   │   │
│   │   └─ NO  → Execute via GENERAL-PURPOSE AGENT (with skill protocol loaded)
│   │             Skill provides: protocol, templates, quality criteria
│   │             Agent provides: flexible execution across tools
│
└─ No matching skill?
    └─ Select SPECIALIZED AGENT directly (Explore, Plan, frontend-styling-expert, etc.)
    └─ Or GENERAL-PURPOSE as last resort
```
