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
# TITLE
# --------------------------------------------------

st.title("💻 CodeAI Assistant")
st.write(
    "Generative AI-Based Code Explanation & Documentation Assistant"
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    language = st.selectbox(
        "💻 Programming Language",
        ["Python", "Java", "C", "C++"]
    )

    st.divider()

    st.info(
        "CodeAI helps students understand, "
        "document, debug and improve source code."
    )

# --------------------------------------------------
# CODE INPUT
# --------------------------------------------------

st.subheader("📝 Enter Your Code")

code = st.text_area(
    "Paste your source code below:",
    height=300,
    placeholder="""Example:

def add(a, b):
    return a + b

print(add(10, 20))
""",
    label_visibility="collapsed"
)

# --------------------------------------------------
# AI TASK
# --------------------------------------------------

st.subheader("🤖 Select an AI Task")

task = st.selectbox(
    "Choose what you want CodeAI to do:",
    [
        "💡 Explain Code",
        "🔎 Line-by-Line Explanation",
        "📚 Generate Documentation",
        "🐛 Find Bugs & Potential Issues",
        "📊 Analyze Code Quality",
        "⚡ Improve Code"
    ]
)

st.divider()

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

if st.button(
    "🚀 Generate AI Result",
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

            # Connect to Gemini
            client = genai.Client(
                api_key=api_key
            )

            # Remove emojis before sending task to AI
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
            # AI PROMPT
            # --------------------------------------------------

            prompt = f"""
You are CodeAI, an expert programming assistant
helping a college student understand source code.

Programming Language:
{language}

User's Code:
{code}

Requested Task:
{clean_task}

Give a clear, accurate and beginner-friendly response.

IMPORTANT RULES:
- Use simple language.
- Do not invent information.
- Use Markdown headings and bullet points.
- Put programming code inside code blocks.
- Explain technical terms briefly.

FOR "Explain Code":
- Explain the purpose.
- Explain the main logic.
- Explain important parts.
- Give expected output.
- Give time and space complexity if possible.

FOR "Line-by-Line Explanation":
- Explain each important line separately.
- Show the line or line number.
- Explain what it does in simple language.
- Give expected output if useful.

FOR "Generate Documentation":
- Give a project/function description.
- Explain inputs.
- Explain outputs.
- Explain functions/classes.
- Mention requirements or dependencies if visible.

FOR "Find Bugs & Potential Issues":
- Identify possible errors or bugs.
- Mention the affected line or section.
- Explain why it is a problem.
- Provide a suggested fix.
- Mention edge cases when relevant.
- If there are no obvious problems, clearly say so.

FOR "Analyze Code Quality":
Analyze:
- Readability
- Maintainability
- Efficiency
- Possible security concerns
- Time complexity
- Space complexity
- Suggestions for improvement

FOR "Improve Code":
- Provide improved code.
- Keep it understandable for a student.
- Explain the major changes.
- Explain why the changes are useful.
- Preserve the original purpose of the program.

End with a short "Summary" section.
"""

            # --------------------------------------------------
            # GENERATE RESPONSE
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
            # DISPLAY RESULT
            # --------------------------------------------------

            st.subheader("🤖 AI Generated Result")

            st.markdown(result)

            # --------------------------------------------------
            # DOWNLOAD
            # --------------------------------------------------

            st.download_button(
                label="📥 Download Result",
                data=result,
                file_name="CodeAI_Result.txt",
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
    "CodeAI Assistant | Generative AI for "
    "Understanding, Documenting, Debugging and Improving Code"
)