def summarize_issues(style_issues, complexity_results):
    points = []

    # flake8 issues
    if style_issues:
        points.append(f"Found {len(style_issues)} style/lint issues.")
    else:
        points.append("No flake8 lint issues found.")

    # complexity results
    comps = complexity_results["complexities"]
    if comps:
        high = [c for c in comps if c["rank"] in ["D", "E", "F"]]
        if high:
            names = ", ".join([c["name"] for c in high])
            points.append(f"High complexity in functions: {names}.")
        else:
            points.append("All functions have acceptable complexity.")
    else:
        points.append("No functions/classes found for complexity analysis.")

    # maintainability index
    mi = complexity_results["maintainability_index"]
    if mi:
        points.append(f"Maintainability Index: {mi:.2f}")

    return points
def compute_code_quality_score(style_issues, complexity_results):
    issue_count = len(style_issues)
    if issue_count == 0:
        style_score = 10
    elif issue_count <= 5:
        style_score = 8
    elif issue_count <= 10:
        style_score = 6
    elif issue_count <= 20:
        style_score = 4
    else:
        style_score = 2

    complexities = complexity_results["complexities"]
    worst_rank = "A"
    ranks = ["A", "B", "C", "D", "E", "F"]

    for c in complexities:
        if ranks.index(c["rank"]) > ranks.index(worst_rank):
            worst_rank = c["rank"]

    complexity_map = {
        "A": 10, "B": 9, "C": 7, "D": 5, "E": 3, "F": 1
    }
    complexity_score = complexity_map.get(worst_rank, 5)

    mi = complexity_results["maintainability_index"] or 50
    if mi >= 80:
        mi_score = 10
    elif mi >= 70:
        mi_score = 8
    elif mi >= 60:
        mi_score = 6
    elif mi >= 40:
        mi_score = 4
    else:
        mi_score = 2

    final_score = (
        style_score * 0.4 +
        complexity_score * 0.4 +
        mi_score * 0.2
    )

    return round(final_score, 1)
