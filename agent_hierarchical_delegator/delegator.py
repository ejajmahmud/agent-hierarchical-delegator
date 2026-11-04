"""Recursive hierarchical task delegator."""
from typing import Dict, List, Any


class HierarchicalDelegator:
    def __init__(self):
        self._specialists: Dict[str, List[str]] = {}

    def register_specialist(self, agent_id: str, capabilities: List[str]):
        self._specialists[agent_id] = capabilities

    def find_best_agent(self, required_capability: str) -> str:
        for agent_id, caps in self._specialists.items():
            if required_capability in caps:
                return agent_id
        return "general_worker"

    def plan_delegation(self, subtasks: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        plan = []
        for task in subtasks:
            agent = self.find_best_agent(task.get("capability", ""))
            plan.append({
                "task_name": task.get("name"),
                "assigned_agent": agent,
                "status": "ASSIGNED"
            })
        return plan
