import os
import json
from groq import Groq
from dotenv import load_dotenv
from models import CommunityProfile, PathBResult

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_community(profile: CommunityProfile):
    prompt = f"""You are a public policy AI advisor analyzing community AI readiness.

Community: {profile.name}
Type: {profile.community_type} | Population: {profile.population}
Scores: Infrastructure={profile.infrastructure}, Workforce={profile.workforce},
Data Maturity={profile.data_maturity}, Governance={profile.governance},
Ethics={profile.ethics}, Public Trust={profile.public_trust}
Additional context: {profile.free_text or 'None provided'}

Analyze this community and respond in JSON only. No markdown, no backticks, no preamble.
Respond with exactly this structure:
{{
    "analysis": "2-3 sentence contextual assessment of this community's AI readiness",
    "similar_cases": [
        {{"name": "City/County name", "outcome": "what happened", "relevance": "why this is relevant"}},
        {{"name": "City/County name", "outcome": "what happened", "relevance": "why this is relevant"}}
    ],
    "recommendations": ["specific recommendation 1", "specific recommendation 2", "specific recommendation 3"],
    "non_ai_alternatives": ["non-AI alternative 1", "non-AI alternative 2"],
    "dimension_estimates": {{
        "infrastructure": 0,
        "workforce": 0,
        "data_maturity": 0,
        "governance": 0,
        "ethics": 0,
        "public_trust": 0
    }}
}}

For dimension_estimates, provide your independent assessment (0-100) of each dimension based on
contextual analysis of similar communities. These may differ from the self-reported scores above
if patterns from similar communities suggest the self-reported scores are optimistic or conservative."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        raw = response.choices[0].message.content
        data = json.loads(raw)
        path_b = PathBResult(
            analysis=data["analysis"],
            similar_cases=data["similar_cases"],
            recommendations=data["recommendations"],
            non_ai_alternatives=data["non_ai_alternatives"]
        )
        return path_b, data.get("dimension_estimates", {})

    except Exception as e:
        print(f"LLM Error: {e}")
        # Fallback if Groq fails
        fallback = PathBResult(
            analysis="Unable to generate contextual analysis. Using deterministic scoring only.",
            similar_cases=[],
            recommendations=["Conduct a manual readiness assessment with local stakeholders"],
            non_ai_alternatives=["Form a community advisory panel for technology decisions"]
        )
        return fallback, {}