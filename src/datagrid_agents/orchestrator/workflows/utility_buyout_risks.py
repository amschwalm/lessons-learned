"""Utility / electrical package buyout risk playbook."""

from __future__ import annotations

from datagrid_agents.orchestrator.parallel import AgentCall
from datagrid_agents.orchestrator.registry import load_role

WORKFLOW = "utility_buyout_risks"

ROLES = ("mentor", "schedule", "change_order")

SHARED_INSTRUCTIONS = """
You are contributing to a multi-agent buyout risk review for an electrical /
utility package. Focus only on your specialty. Prefer concrete, field-proven
risks over generic advice. When possible, cite project patterns or lesson themes
from knowledge available to you.

Respond with:
1. A short specialty framing (2-4 sentences)
2. A markdown table of the top risks from YOUR specialty (max 5), with columns:
   Risk | Why it matters | Preventative action
3. One recommended next action for the project team
""".strip()


def build_prompt(user_goal: str, context: str, role_key: str) -> str:
    """Build a role-specific prompt including optional local context."""
    role = load_role(role_key)
    parts = [
        SHARED_INSTRUCTIONS,
        "",
        f"Your role key: {role.key}",
        f"Your specialty: {role.role}",
        f"Agent name: {role.name}",
        "",
        "## User goal",
        user_goal.strip(),
    ]
    if context.strip():
        parts.extend(["", context.strip()])
    return "\n".join(parts)


def build_calls(user_goal: str, context: str = "") -> list[AgentCall]:
    """Create parallel Datagrid calls for the utility buyout workflow."""
    calls: list[AgentCall] = []
    for role_key in ROLES:
        role = load_role(role_key)
        calls.append(
            AgentCall(
                role=role.key,
                agent_id=role.id,
                prompt=build_prompt(user_goal, context, role_key),
                chat_mode=role.chat_mode,
            )
        )
    return calls
