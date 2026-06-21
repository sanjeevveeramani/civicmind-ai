from models import CommunityProfile, PathAResult

BASELINES = {
    "urban": {
        "infrastructure": 72, "workforce": 65, "data_maturity": 60,
        "governance": 55, "ethics": 50, "public_trust": 58
    },
    "suburban": {
        "infrastructure": 58, "workforce": 50, "data_maturity": 45,
        "governance": 42, "ethics": 38, "public_trust": 52
    },
    "rural": {
        "infrastructure": 35, "workforce": 30, "data_maturity": 25,
        "governance": 28, "ethics": 22, "public_trust": 45
    }
}

ACTION_TEMPLATES = {
    "infrastructure": {
        "quick": "Audit current broadband coverage and identify connectivity dead zones",
        "medium": "Partner with ISPs for subsidized connectivity programs in underserved areas",
        "long": "Deploy municipal broadband infrastructure to ensure universal access"
    },
    "workforce": {
        "quick": "Survey existing staff for AI literacy levels and identify skill gaps",
        "medium": "Launch AI training partnerships with local universities and community colleges",
        "long": "Establish a dedicated AI talent pipeline with internship and apprenticeship programs"
    },
    "data_maturity": {
        "quick": "Inventory all departmental data assets and identify digitization priorities",
        "medium": "Implement unified data governance standards across all departments",
        "long": "Build a centralized data lake with cross-department sharing and analytics capabilities"
    },
    "governance": {
        "quick": "Form an AI oversight committee with representatives from each department",
        "medium": "Draft and adopt a formal AI use policy with review and approval processes",
        "long": "Establish a permanent AI governance board with external advisory members"
    },
    "ethics": {
        "quick": "Publish a public statement on AI ethics principles the community will follow",
        "medium": "Implement bias auditing procedures for any AI system before deployment",
        "long": "Create a standing ethics review board with community representation"
    },
    "public_trust": {
        "quick": "Host a town hall to discuss AI plans and gather community feedback",
        "medium": "Launch a public dashboard showing how AI is being used in community services",
        "long": "Establish a community AI advisory panel with elected resident representatives"
    }
}

def generate_gaps(profile: CommunityProfile, path_a_result: PathAResult):
    baseline = BASELINES.get(profile.community_type, BASELINES["suburban"])
    percentiles = {}
    actions = {"quick_wins": [], "medium_term": [], "long_term": []}

    for dim_score in path_a_result.dimensions:
        dim = dim_score.dimension
        base = baseline[dim]
        pct = min(99, max(1, int((dim_score.score / max(base, 1)) * 50)))
        percentiles[dim] = {
            "score": dim_score.score,
            "baseline": base,
            "percentile": pct,
            "comparison": (
                f"Your community scored {dim_score.score}/100 on {dim}. "
                f"The average for {profile.community_type} communities is {base}/100, "
                f"placing you at the {pct}th percentile."
            )
        }
        if dim_score.score < 40:
            tmpl = ACTION_TEMPLATES[dim]
            actions["quick_wins"].append({"dimension": dim, "action": tmpl["quick"]})
            actions["medium_term"].append({"dimension": dim, "action": tmpl["medium"]})
            actions["long_term"].append({"dimension": dim, "action": tmpl["long"]})
        elif dim_score.score < 70:
            tmpl = ACTION_TEMPLATES[dim]
            actions["medium_term"].append({"dimension": dim, "action": tmpl["medium"]})
            actions["long_term"].append({"dimension": dim, "action": tmpl["long"]})

    return {
        "community": profile.name,
        "community_type": profile.community_type,
        "percentiles": percentiles,
        "action_plan": actions
    }