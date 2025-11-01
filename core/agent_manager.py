import toml
from pathlib import Path
from typing import Dict, Any

from agents.web_agent import WebAgent
from agents.finance_agent import FinanceAgent
from agents.translator_agent import TranslatorAgent


class AgentManager:
    """Keeps a registry of available agents and routes tasks to them."""

    def __init__(self, config_path: str = "config.toml"):
        config_file = Path(config_path)
        if config_file.exists():
            self.config = toml.loads(config_file.read_text(encoding="utf-8"))
        else:
            self.config = {}

        self.agents = {
            "web": WebAgent(self.config),
            "finance": FinanceAgent(self.config),
            "translator": TranslatorAgent(self.config),
        }

    def list_agents(self):
        return list(self.agents.keys())

    def run(self, agent_name: str, query: str) -> Dict[str, Any]:
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Unknown agent: {agent_name}")
        return agent.run(query)