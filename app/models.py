from pydantic import BaseModel

class Suggestion(BaseModel):
    job_suggestion: str
    confidence: float
