from models import PathAResult, ArbitratorResult

DIVERGENCE_THRESHOLD = 20

def arbitrate(path_a: PathAResult, path_b_estimates: dict) -> ArbitratorResult:
    divergences = []
    for dim_score in path_a.dimensions:
        dim = dim_score.dimension
        a_score = dim_score.score
        b_score = path_b_estimates.get(dim, a_score)
        diff = abs(a_score - b_score)
        if diff >= DIVERGENCE_THRESHOLD:
            divergences.append({
                "dimension": dim,
                "path_a_score": a_score,
                "path_b_score": b_score,
                "difference": diff,
                "explanation": (
                    f"Path A scored {dim} at {a_score} based on structured self-reported data. "
                    f"Path B estimated {b_score} based on contextual analysis of similar communities. "
                    f"A gap of {diff} points suggests the structured score may not capture "
                    f"qualitative factors such as implementation effectiveness or political readiness."
                )
            })
    return ArbitratorResult(
        status="divergence" if divergences else "agreement",
        divergences=divergences,
        confidence="needs_review" if divergences else "high"
    )