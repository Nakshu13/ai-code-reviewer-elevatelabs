import datetime

def generate_report(code, style_issues, formatted_code, complexity, summary):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []

    lines.append("# AI Code Review Report")
    lines.append(f"Generated: {t}\n")

    lines.append("## Summary")
    for p in summary:
        lines.append(f"- {p}")
    lines.append("")

    lines.append("## Flake8 Issues")
    if style_issues:
        for i, iss in enumerate(style_issues, 1):
            lines.append(f"{i}. Line {iss['line']} Col {iss['col']} — {iss['code']}: {iss['message']}")
    else:
        lines.append("No issues.")
    lines.append("")

    lines.append("## Complexity")
    lines.append(f"Maintainability Index: {complexity['maintainability_index']}")
    lines.append("")

    lines.append("### Functions")
    for c in complexity["complexities"]:
        lines.append(f"- {c['name']} (line {c['lineno']}): complexity {c['complexity']} ({c['rank']})")

    lines.append("\n## Original Code\n```python")
    lines.append(code)
    lines.append("```")

    lines.append("\n## Formatted Code (Black)\n```python")
    lines.append(formatted_code)
    lines.append("```")

    return "\n".join(lines)
