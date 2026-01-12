from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class AgentInput(BaseModel):
    resume_text: str = Field(..., min_length=50)
    job_description: str = Field(..., min_length=50)


class StepResult(BaseModel):
    step_name: str
    decision: str
    output: Dict[str, Any]
    score: float = 0.0
    feedback: Optional[str] = None


class FinalAgentReport(BaseModel):
    workflow_type: str
    final_score: float
    steps: List[StepResult]
    final_output: Dict[str, Any]
