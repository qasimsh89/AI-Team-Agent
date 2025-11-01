from duckduckgo_search import DDGS
from typing import Dict, Any, List


class WebAgent:
    def __init__(self, config: dict):
        self.config = config

    def _search(self, query: str, max_results: int = 5) -> List[dict]:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=max_results))

    def run(self, query: str) -> Dict[str, Any]:
        results = self._search(query)
        return {
            "agent": "web",
            "query": query,
            "results": results,
        }