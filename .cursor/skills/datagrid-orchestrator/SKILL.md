---
name: datagrid-orchestrator
description: Orchestrate parallel Datagrid API agent calls with local repository context and Cursor-only operations. Use when coordinating Datagrid agents, running hybrid construction workflows (buyout risks, RFI/submittal review), or combining knowledge-search agents with code/file analysis.
---

# Datagrid Orchestrator

Cursor owns planning, parallelism, local code context, and repo operations.
Datagrid agents own domain judgment and knowledge search.

## When to use

- User wants multiple Datagrid agents consulted in parallel
- A construction workflow needs lessons learned + schedule + change-order views
- Local files/code should supplement Datagrid prompts
- Follow-on work must happen in the repo (write checklist, open PR, run tests)

## Quick commands

From the repo root (venv recommended):

```bash
export DATAGRID_API_KEY="${DATAGRID_API_KEY:-$Datagrid_API_KEY}"
.venv/bin/datagrid-agents roles
.venv/bin/datagrid-agents workflows
.venv/bin/datagrid-agents orchestrate utility_buyout_risks \
  -p "<user goal>" \
  -c path/to/local/context
```

Or use the skill wrapper:

```bash
python .cursor/skills/datagrid-orchestrator/scripts/run_workflow.py \
  utility_buyout_risks \
  -p "<user goal>" \
  -c path/to/file
```

## Operating procedure

1. **Clarify the goal** — package/trade, decision needed, and any local files.
2. **Pick a workflow** — start with `utility_buyout_risks` when relevant; otherwise compose role calls via `roles` + targeted `run`.
3. **Attach local context** — use `-c` for buyout notes, scope excerpts, schedule snippets, or open questions in the repo.
4. **Run orchestration** — prefer `datagrid-agents orchestrate <workflow>` for parallel fan-out.
5. **Synthesize** — read the merged markdown/JSON under `.orchestrator/runs/` (or stdout). Deduplicate risks across agents and highlight conflicts.
6. **Differential Cursor ops** — after Datagrid returns, do what Datagrid cannot:
   - write a checklist or risk register into the repo
   - compare claims against local files
   - run tests/scripts
   - open a PR with artifacts
7. **Follow up** — reuse `conversation_id` values from the run JSON when continuing with one agent.

## Guardrails

- Do **not** recreate Datagrid agents from Cursor unless the user asks; IDs live in `src/datagrid_agents/orchestrator/agents.yaml`.
- Prefer role keys (`mentor`, `schedule`, `change_order`) over hardcoding UUIDs in chat.
- Cap parallelism (`--max-workers`, default 3).
- Never print API keys.
- For expensive runs, prefer saving artifacts (`orchestrate` does this by default).

## References

- Role registry details: `references/agents.md`
- Workflow catalog: `references/workflows.md`
