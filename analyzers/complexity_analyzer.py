from radon.complexity import cc_visit, cc_rank
from radon.metrics import mi_visit

def analyze_complexity(code: str):
    results = cc_visit(code)
    complexities = []

    for block in results:
        complexities.append({
            "name": block.name,
            "lineno": block.lineno,
            "complexity": block.complexity,
            "rank": cc_rank(block.complexity)
        })

    try:
        mi = mi_visit(code, True)
    except:
        mi = None

    return {
        "complexities": complexities,
        "maintainability_index": mi
    }
