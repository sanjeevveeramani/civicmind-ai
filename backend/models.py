from pydantic import BaseModel, Field
from typing import Optional

class CommunityProfile(BaseModel):
    name: str
    population: int
    community_type: str  # urban / suburban / rural
    infrastructure: int = Field(ge=0, le=100)
    workforce: int = Field(ge=0, le=100)
    data_maturity: int = Field(ge=0, le=100)
    governance: int = Field(ge=0, le=100)
    ethics: int = Field(ge=0, le=100)
    public_trust: int = Field(ge=0, le=100)
    free_text: Optional[str] = None

class DimensionScore(BaseModel):
    dimension: str
    score: int
    reasoning: str
    weight: float
    weighted_score: float

class PathAResult(BaseModel):
    dimensions: list[DimensionScore]
    overall_score: float

class PathBResult(BaseModel):
    analysis: str
    similar_cases: list[dict]
    recommendations: list[str]
    non_ai_alternatives: list[str]

class ArbitratorResult(BaseModel):
    status: str  # 'agreement' or 'divergence'
    divergences: list[dict]
    confidence: str  # 'high' or 'needs_review'

class ScoringResponse(BaseModel):
    path_a: PathAResult
    path_b: PathBResult
    arbitrator: ArbitratorResult