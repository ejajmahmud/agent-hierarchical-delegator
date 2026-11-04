"""CLI for agent-hierarchical-delegator."""
import sys
import argparse
from .delegator import HierarchicalDelegator


def main():
    parser = argparse.ArgumentParser(description="Agent Hierarchical Delegator")
    parser.add_argument("--demo", action="store_true", help="Run delegation demo")
    args = parser.parse_args()

    d = HierarchicalDelegator()
    d.register_specialist("coder_bot", ["python", "rust"])
    d.register_specialist("db_bot", ["sql", "postgres"])
    plan = d.plan_delegation([{"name": "setup_db", "capability": "sql"}])
    print(f"Delegation Plan: {plan}")
    sys.exit(0)


if __name__ == "__main__":
    main()
