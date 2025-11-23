import tempfile
from flake8.api import legacy as flake8
import black
from black import FileMode

def run_style_checks(code: str):
    style_guide = flake8.get_style_guide()

    # Write code to temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        file_path = tmp.name

    # Run flake8
    report = style_guide.check_files([file_path])

    issues = []

    # SAFE for all flake8 versions
    stats = report.get_statistics("")

    for stat in stats:
        # Example stat: "E302 expected 2 blank lines, found 1"
        parts = stat.split(" ", 1)
        error_code = parts[0]
        message = parts[1] if len(parts) > 1 else ""

        issues.append({
            "code": error_code,
            "message": message,
            "line": "-",
            "col": "-"
        })

    return issues


def format_code_with_black(code: str):
    try:
        return black.format_str(code, mode=FileMode())
    except Exception:
        return code
