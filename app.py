import streamlit as st
from google import genai

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="CodeAI Assistant",
    page_icon="💻",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Main title */
.title {
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
    color: #ffffff;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #9ca3af;
    margin-bottom: 30px;
}

/* Feature cards */
.feature-card {
    padding: 20px 12px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    background: #ffffff;
    color: #111827;
    text-align: center;
    min-height: 115px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 5px;
}

.feature-title {
    font-size: 17px;
    font-weight: 700;
    color: #111827;
}

.feature-text {
    font-size: 13px;
    color: #6b7280;
}

/* Section headings */
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 10px;
}

/* Result box */
.result-card {
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    background-color: #fafafa;
    margin-top: 10px;
}

/* Buttons */
.stButton > button {
    height: 48px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 700;
}

.stDownloadButton > button {
    border-radius: 10px;
    font-weight: 600;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">💻 CodeAI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Generative AI-Based Code Explanation & Documentation Assistant'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <div class="feature-title">Explain</div>
        <div class="feature-text">Understand your code</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🐛</div>
        <div class="feature-title">Debug</div>
        <div class="feature-text">Find potential issues</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Document</div>
        <div class="feature-text">Generate documentation</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Improve</div>
        <div class="feature-text">Improve your code</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Project Settings")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Enter your API key"
    )

    language = st.selectbox(
        "💻 Programming Language",
        ["Python", "Java", "C", "C++"]
    )

    st.divider()

    st.markdown("### 🧠 About CodeAI")

    st.write(
        "CodeAI uses Generative AI to help students "
        "understand, document, debug and improve source code."
    )

    st.divider()

    st.caption("Supported Languages")

    st.write("🐍 Python")
    st.write("☕ Java")
    st.write("©️ C")
    st.write("⚙️ C++")

# --------------------------------------------------
# CODE WORKSPACE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📝 Code Workspace</div>',
    unsafe_allow_html=True
)

st.caption(
    "Paste your source code below and select an AI operation."
)

code = st.text_area(
    "Source Code",
    height=320,
    placeholder="""Example:

def add(a, b):
    return a + b

print(add(10, 20))
""",
    label_visibility="collapsed"
)

# --------------------------------------------------
# TASK SELECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🤖 AI Operation</div>',
    unsafe_allow_html=True
)

task = st.selectbox(
    "Choose what CodeAI should do:",
    [
        "💡 Explain Code",
        "🔎 Line-by-Line Explanation",
        "📚 Generate Documentation",
        "🐛 Find Bugs & Potential Issues",
        "📊 Analyze Code Quality",
        "⚡ Improve Code"
    ]
)

st.write("")

# --------------------------------------------------
# GENERATE RESULT
# --------------------------------------------------

if st.button(
    "🚀 Analyze Code",
    use_container_width=True
):

    if not api_key:

        st.error(
            "Please enter your Gemini API key in the sidebar."
        )

    elif not code.strip():

        st.warning(
            "Please paste some code first."
        )

    else:

        try:

            client = genai.Client(
                api_key=api_key
            )

            # --------------------------------------------------
            # REMOVE EMOJI FROM TASK NAME
            # --------------------------------------------------

            clean_task = (
                task
                .replace("💡 ", "")
                .replace("🔎 ", "")
                .replace("📚 ", "")
                .replace("🐛 ", "")
                .replace("📊 ", "")
                .replace("⚡ ", "")
            )

            # --------------------------------------------------
            # TASK-SPECIFIC INSTRUCTIONS
            # --------------------------------------------------

            if clean_task == "Explain Code":

                task_instruction = """
Explain ONLY the code.

Include:
1. Purpose
2. Main logic
3. Important parts
4. Expected output

Do NOT provide bug detection, documentation,
code improvement, or code quality analysis.
"""

            elif clean_task == "Line-by-Line Explanation":

                task_instruction = """
Explain ONLY the code line by line.

For each important line:
1. Show the line
2. Explain what it does
3. Explain why it is used

Do NOT provide separate bug detection,
documentation, code improvement, or code quality analysis.
"""

            elif clean_task == "Generate Documentation":

                task_instruction = """
Generate ONLY documentation for the EXACT code provided.

Include:
1. Description
2. Inputs
3. Outputs
4. Functions/classes
5. Requirements

IMPORTANT:
- Use the exact function, class, variable and parameter names
  from the provided code.
- Do not use names from previous examples.
- Do not invent functions or variables.
- Do not rename functions or variables.

Do NOT provide general code explanation,
bug detection, code improvement, or code quality analysis.
"""

            elif clean_task == "Find Bugs & Potential Issues":

                task_instruction = """
Find ONLY bugs and potential issues.

For each issue:
1. Identify the affected line or section
2. Explain the problem
3. Explain why it may occur
4. Give a suggested fix
5. Mention important edge cases

If there are no obvious issues, clearly state that.

Do NOT provide general documentation or
unrelated code quality analysis.
"""

            elif clean_task == "Analyze Code Quality":

                task_instruction = """
Analyze ONLY the quality of the code.

Evaluate:
1. Readability
2. Maintainability
3. Efficiency
4. Security concerns
5. Time complexity
6. Space complexity
7. Improvement suggestions

Do NOT rewrite the complete code.
Do NOT provide separate documentation or
line-by-line explanation.
"""

            else:

                task_instruction = """
Improve ONLY the provided code.

Include:
1. Improved code
2. Explanation of the important changes
3. Why the changes are useful

Keep the original purpose of the program.

Do NOT provide separate bug reports,
documentation, or line-by-line analysis.
"""

            # --------------------------------------------------
            # FINAL PROMPT
            # --------------------------------------------------

            prompt = f"""
You are CodeAI, a professional programming assistant
designed to help college students.

Programming Language:
{language}

User's Code:
{code}

Selected Operation:
{clean_task}

IMPORTANT:
The user selected ONLY "{clean_task}".

{task_instruction}

GENERAL RULES:
- Follow ONLY the selected operation.
- Do not answer other operations.
- Do not add unrelated sections.
- Use simple beginner-friendly language.
- Use Markdown headings and bullet points.
- Put code inside proper code blocks.
- Do not invent information.
"""

            # --------------------------------------------------
            # AI GENERATION
            # --------------------------------------------------

            with st.spinner(
                "🤖 CodeAI is analyzing your code..."
            ):

                interaction = client.interactions.create(
                    model="gemini-3.5-flash-lite",
                    input=prompt
                )

            result = interaction.output_text

            # --------------------------------------------------
            # RESULT
            # --------------------------------------------------

            st.divider()

            st.markdown(
                '<div class="section-title">🤖 AI Analysis</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="result-card">',
                unsafe_allow_html=True
            )

            st.markdown(result)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            st.write("")

            # --------------------------------------------------
            # DOWNLOAD
            # --------------------------------------------------

            st.download_button(
                label="📥 Download Analysis",
                data=result,
                file_name="CodeAI_Analysis.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "CodeAI Assistant • Generative AI for "
    "Code Understanding, Documentation, Debugging & Improvement"
)