"""Tests for agent-hierarchical-delegator."""
import unittest
from agent_hierarchical_delegator.delegator import HierarchicalDelegator


class TestHierarchicalDelegator(unittest.TestCase):
    def setUp(self):
        self.d = HierarchicalDelegator()
        self.d.register_specialist("sql_agent", ["db", "postgres"])
        self.d.register_specialist("ui_agent", ["react", "css"])

    def test_delegation_assignment(self):
        tasks = [
            {"name": "create_tables", "capability": "db"},
            {"name": "build_button", "capability": "react"}
        ]
        plan = self.d.plan_delegation(tasks)
        self.assertEqual(plan[0]["assigned_agent"], "sql_agent")
        self.assertEqual(plan[1]["assigned_agent"], "ui_agent")


if __name__ == "__main__":
    unittest.main()
