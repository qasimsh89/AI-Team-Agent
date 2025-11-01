from typing import Dict, Any
import yfinance as yf


class FinanceAgent:
    def __init__(self, config: dict):
        self.config = config

    def run(self, query: str) -> Dict[str, Any]:
        # naive: assume the query is a ticker
        ticker = query.strip().upper()
        info = {}
        try:
            data = yf.Ticker(ticker)
            price = data.history(period="1d")["Close"].iloc[-1]
            info = {"ticker": ticker, "price": float(price)}
        except Exception as e:
            info = {"error": str(e), "ticker": ticker}
        return {
            "agent": "finance",
            "query": query,
            "data": info,
        }