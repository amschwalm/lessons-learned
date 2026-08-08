# Orchestrator agent roles

Source of truth: `src/datagrid_agents/orchestrator/agents.yaml`

Override any role id with `DATAGRID_AGENT_<ROLE>` (example: `DATAGRID_AGENT_MENTOR`).

| Key | Specialty | Typical use |
| --- | --- | --- |
| `mentor` | Lessons learned | Buyout pitfalls, historical risk patterns |
| `schedule` | Schedule risk | Lead times, utility coordination delays, CP impact |
| `change_order` | Change orders | Documentation/pricing gaps that become COs |
| `deep_search` | Project search | Specs/drawings/RFI/submittal grounded answers |
| `drawings_specs` | Drawings & specs | Callouts, materials, annotation search |
| `submittal` | Submittal review | Spec vs product compliance |

List live mapping:

```bash
.venv/bin/datagrid-agents roles
```
