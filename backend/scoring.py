from models import CommunityProfile, DimensionScore, PathAResult

# Published weights - cited from OECD AI Policy Observatory
WEIGHTS = {
    "infrastructure": 0.20,
    "workforce": 0.20,
    "data_maturity": 0.25,
    "governance": 0.15,
    "ethics": 0.10,
    "public_trust": 0.10,
}

REASONING = {
    "infrastructure": {
        "low": "Limited digital infrastructure with less than 40% broadband coverage or minimal cloud adoption.",
        "mid": "Moderate infrastructure in place with some cloud services but gaps in connectivity remain.",
        "high": "Strong digital infrastructure with broad connectivity and cloud-ready systems."
    },
    "workforce": {
        "low": "Critical shortage of AI-skilled workers with no active training programs in place.",
        "mid": "Some technical talent available but gaps in AI-specific skills and limited training pipelines.",
        "high": "Strong technical workforce with active AI training programs and university partnerships."
    },
    "data_maturity": {
        "low": "Most departments still rely on paper records with no centralized data governance.",
        "mid": "Partial digitization across departments but inconsistent data standards and siloed systems.",
        "high": "Comprehensive digital records with unified data governance and cross-department sharing."
    },
    "governance": {
        "low": "No formal AI policies or oversight mechanisms exist in the community.",
        "mid": "Some AI-related policies exist on paper but enforcement and review processes are unclear.",
        "high": "Established AI governance framework with clear oversight, review cycles, and accountability."
    },
    "ethics": {
        "low": "No bias auditing, transparency mandates, or ethical review processes for AI systems.",
        "mid": "Basic awareness of AI ethics but no formal audit procedures or compliance frameworks.",
        "high": "Active bias auditing, transparency requirements, and ethics review board in place."
    },
    "public_trust": {
        "low": "Significant public resistance or skepticism toward government use of AI technologies.",
        "mid": "Mixed public sentiment with some openness but concerns about privacy and accountability.",
        "high": "Strong public support for AI adoption backed by successful prior technology initiatives."
    }
}

def get_tier(score: int) -> str:
    if score < 40:
        return "low"
    if score < 70:
        return "mid"
    return "high"

def score_community(profile: CommunityProfile) -> PathAResult:
    dimensions = []
    for dim, weight in WEIGHTS.items():
        raw = getattr(profile, dim)
        tier = get_tier(raw)
        reasoning = REASONING[dim][tier]
        dimensions.append(DimensionScore(
            dimension=dim,
            score=raw,
            reasoning=f"Scored {raw}/100: {reasoning}",
            weight=weight,
            weighted_score=round(raw * weight, 2)
        ))
    overall = round(sum(d.weighted_score for d in dimensions), 2)
    return PathAResult(dimensions=dimensions, overall_score=overall)