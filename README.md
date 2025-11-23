### AI Code Reviewer

A simple and interactive web application that automatically reviews Python code for style, formatting, complexity, and maintainability using static analysis tools. Built with Streamlit, it provides instant feedback, a clean UI, and a downloadable report.

🚀**Features**

🧹 Linting Analysis – Detects PEP8 issues using flake8

🎨 Auto Code Formatting – Formats code using black

📊 Complexity Analysis – Computes cyclomatic complexity via radon

⭐ Code Quality Score – Generates a final score out of 10

📑 Downloadable Report – Full summary in Markdown format

🧭 Modern UI – Tabs, icons, and clean layout built with Streamlit

🛠️ **Tools & Technologies**

Python 3.9+

Streamlit

flake8

black

radon

VS Code

📁 **Project Structure**

ai-code-reviewer/
│
├── app.py
├── analyzers/
│   ├── style_analyzer.py
│   └── complexity_analyzer.py
├── utils/
│   ├── summary.py
│   └── report.py
└── requirements.txt

▶️ How to Run

1. Create & activate virtual environment

python -m venv venv
venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

**Usage**

 Paste Python code or upload a .py file

 Click Analyze Code

 View results in tabs:

 Summary

 Style & Lint Issues

 Original vs Formatted Code

 Complexity Metrics

 Download the review report

📦 Output Includes

 Lint warnings

 Auto-formatted code

 Code complexity rank

 Maintainability Index

 Final Code Quality Score (/10)

 Full report in Markdown
