#  2026 Julius Cameron Hill / TitanU AI LLC. All rights reserved. Patent pending JCH-2026-001.
from agents.core.base_agent import BaseAgent
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonalFinanceTherapistAgent(BaseAgent):
    def __init__(self):
        super().__init__("agent-04-Personal-Finance-Therapist") 
    def analyze_spending(self, transactions: list) -> dict:
        total = sum(t.get("amount", 0) for t in transactions)
        return {"total_spent": total, "count": len(transactions)}
        for attr in dir(self):
            if callable(getattr(self, attr)) and not attr.startswith("__") and attr not in ["execute", "register_tool", "call_tool", "success", "failure", "telemetry"]:
                self.register_tool(attr, getattr(self, attr))

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            logger.info(f"Processing payload execution on agent: {self.name}") 
            txns = payload.get("transactions", [])
            analysis = self.call_tool("analyze_spending", transactions=txns)
            return self.success(analysis)
        except Exception as e:
            logger.error(f"Execution failed on agent {self.name}: {str(e)}")
            return self.failure(str(e))
