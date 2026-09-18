# 💻 CodeAI Assistant

### Generative AI-Based Code Explanation & Documentation Assistant

CodeAI Assistant is a Generative AI-powered programming assistant designed to help students understand, debug, document, analyze, and improve source code.

The application uses Python, Streamlit, and the Gemini API to provide AI-powered code assistance through a simple web interface.

---

## 🚀 Features

### 💡 Explain Code
Provides a simple explanation of the purpose, logic, important parts, and expected output of the given code.

### 🔎 Line-by-Line Explanation
Explains the important lines of source code individually and describes what each line does.

### 📚 Generate Documentation
Automatically generates documentation containing:
- Description
- Inputs
- Outputs
- Functions/classes
- Requirements

### 🐛 Find Bugs & Potential Issues
Identifies possible programming errors and explains:
- Affected code
- Problem
- Cause
- Suggested fix
- Edge cases

### 📊 Analyze Code Quality
Analyzes:
- Readability
- Maintainability
- Efficiency
- Security concerns
- Time complexity
- Space complexity
- Improvement suggestions

### ⚡ Improve Code
Generates an improved version of the provided code and explains the important changes.

---

## 💻 Supported Programming Languages

- Python
- Java
- C
- C++

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Google Gemini API | Generative AI code analysis |
| HTML/CSS | UI customization |
| Markdown | AI result formatting |

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │      User Input      │
                 │     Source Code      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Streamlit Interface │
                 │  Language Selection  │
                 │  AI Operation        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Prompt Builder    │
                 │ Task-specific Prompt │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Gemini API       │
                 │ Generative AI Model  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    AI Processing     │
                 │ Explain / Debug /    │
                 │ Document / Improve   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     AI Analysis      │
                 │   Displayed to User  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Download Analysis   │
                 └──────────────────────┘