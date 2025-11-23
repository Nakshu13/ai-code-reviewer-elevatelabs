import streamlit as st
from analyzers.style_analyzer import run_style_checks, format_code_with_black
from analyzers.complexity_analyzer import analyze_complexity
from utils.summary import summarize_issues, compute_code_quality_score
from utils.report import generate_report


st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
        🤖 AI Code Reviewer
    </h1>
    <p style='text-align: center; font-size: 18px;'>
       Automatically analyze your Python code for style, complexity, and maintainability.
    </p>
""", unsafe_allow_html=True)

st.title("AI Code Reviewer")

# Input
mode = st.sidebar.radio("Choose input mode:", ["Paste code", "Upload file"])

code = ""
if mode == "Paste code":
    code = st.text_area("Paste your Python code here", height=300)
else:
    uploaded = st.file_uploader("Upload a Python (.py) file", type=["py"])
    if uploaded:
        code = uploaded.read().decode()

# Analyze Button
if st.button("Analyze Code") and code.strip():
    with st.spinner("Processing..."):
        style_issues = run_style_checks(code)
        formatted_code = format_code_with_black(code)
        complexity = analyze_complexity(code)
        summary = summarize_issues(style_issues, complexity)
    # --------------------------
    # 📌 NEW UI + SCORING SYSTEM
    # --------------------------

    score = compute_code_quality_score(style_issues, complexity)

    st.markdown(f"### ⭐ Code Quality Score: **{score}/10**")
    st.progress(score / 10)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📌 Summary", "🧹 Style & Lint", "🎨 Formatting", "📊 Complexity"]
    )

    with tab1:
        st.subheader(" Summary of Issues")
        for p in summary:
            st.markdown(f"- {p}")
        st.markdown(f"### ⭐ Final Score: **{score}/10**")

    with tab2:
        st.subheader("🧹 Flake8 Lint Issues")
        if style_issues:
            st.table(style_issues)
        else:
            st.success("No lint issues found! 🎉")

    with tab3:
        st.subheader("🎨 Original vs Black Formatting")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("####  Original Code")
            st.code(code, language="python")
        with col2:
            st.markdown("####  Formatted Code")
            st.code(formatted_code, language="python")

    with tab4:
        st.subheader("📊 Complexity Analysis (Radon)")
        st.table(complexity["complexities"])
        st.markdown(f"**Maintainability Index:** {complexity['maintainability_index']}")

    # Report download
    report_md = generate_report(code, style_issues, formatted_code, complexity, summary)

    st.download_button(
        label=" Download Code Review Report",
        data=report_md,
        file_name="code_review_report.md",
        mime="text/markdown"
    )
