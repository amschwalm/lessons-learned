# Orchestrator workflows

## `utility_buyout_risks`

**Goal:** Critical risks when buying out an electrical / utility package.

**Parallel Datagrid roles:**
- `mentor` — lessons-learned framing
- `schedule` — timing / utility lead-time risk
- `change_order` — documentation and COR exposure

**Local differential (Cursor):**
- Attach buyout notes / scope excerpts with `-c`
- Merge/dedupe the three specialty tables into one ranked register
- Write checklist artifacts into the repo when the user asks

**Example:**

```bash
.venv/bin/datagrid-agents orchestrate utility_buyout_risks \
  -p "Buying out elec utility package — top risks from lessons learned" \
  -c ./notes/utility-buyout.md
```

## Adding a workflow

1. Create `src/datagrid_agents/orchestrator/workflows/<name>.py` with `build_calls(prompt, context)`.
2. Register it in `workflows/__init__.py`.
3. Document it here and mention it in `SKILL.md` if it is a primary entry point.
