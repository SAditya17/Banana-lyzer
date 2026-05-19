import asyncio
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class AgentResult(BaseModel):
    """
    The result of an agent execution
    """
    output: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)

class Example(BaseModel):
    """
    An example of a web task to evaluate an agent on
    """
    id: str
    url: str
    goal: str
    expected_output: Any
    type: str  # e.g., "detail", "listing", "listing_detail"
    mhtml_path: Optional[str] = None

class AgentRunner:
    """
    Interface for running an agent against a web task
    """
    async def run(self, context: Any, example: Example) -> AgentResult:
        raise NotImplementedError("AgentRunner.run must be implemented")
