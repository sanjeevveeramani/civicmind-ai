from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models import CommunityProfile, ScoringResponse
from scoring import score_community
from llm_service import analyze_community
from arbitrator import arbitrate
from gap_analysis import generate_gaps

load_dotenv()

app = FastAPI(title="CivicMind AI", description="Dual-Path AI Readiness Scoring")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

profiles_db = {}

@app.get("/")
def root():
    return {"message": "CivicMind AI API is running"}

@app.post("/api/profile")
def create_profile(profile: CommunityProfile):
    pid = str(len(profiles_db) + 1)
    profiles_db[pid] = profile
    return {"profile_id": pid, "cpv": profile.model_dump()}

@app.post("/api/score/{profile_id}")
def score(profile_id: str):
    if profile_id not in profiles_db:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile = profiles_db[profile_id]
    path_a = score_community(profile)
    path_b, b_estimates = analyze_community(profile)
    arb = arbitrate(path_a, b_estimates)
    return ScoringResponse(path_a=path_a, path_b=path_b, arbitrator=arb)

@app.get("/api/gaps/{profile_id}")
def gaps(profile_id: str):
    if profile_id not in profiles_db:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile = profiles_db[profile_id]
    path_a = score_community(profile)
    return generate_gaps(profile, path_a)