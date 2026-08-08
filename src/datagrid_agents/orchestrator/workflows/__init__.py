"""Named orchestration playbooks."""

from __future__ import annotations

from typing import Callable

from datagrid_agents.orchestrator.parallel import AgentCall
from datagrid_agents.orchestrator.workflows.utility_buyout_risks import (
    build_calls as build_utility_buyout_risks,
)

WorkflowBuilder = Callable[[str, str], list[AgentCall]]

WORKFLOWS: dict[str, WorkflowBuilder] = {
    "utility_buyout_risks": build_utility_buyout_risks,
}


def list_workflow_names() -> list[str]:
    return sorted(WORKFLOWS)


def get_workflow_builder(name: str) -> WorkflowBuilder:
    try:
        return WORKFLOWS[name]
    except KeyError as exc:
        available = ", ".join(list_workflow_names()) or "(none)"
        raise KeyError(
            f"Unknown workflow '{name}'. Available: {available}"
        ) from exc
