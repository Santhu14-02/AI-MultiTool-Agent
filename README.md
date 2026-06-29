# 🤖 AI MultiTool Agent

An Agentic AI application built with **Python**, **Google Gemini API**, and **Streamlit** that demonstrates the complete AI agent workflow: **Planning → Tool Selection → Tool Execution → Observation → Final Answer**.

The agent intelligently decides which tool to use, executes the tool, observes the result, and produces a final response.

---

## 🚀 Features

* 🧠 AI-powered reasoning using Gemini API
* 📋 Step-by-step planning
* 🛠️ Dynamic tool calling
* 📚 Wikipedia search integration
* 💻 System command execution
* 🌤️ Weather tool (placeholder for future implementation)
* 📄 JSON response parsing
* 🎨 Interactive Streamlit frontend
* 🔍 Displays the complete reasoning process:

  * Raw Model Output
  * Plan
  * Tool Call
  * Observation
  * Final Answer

---

## 🛠️ Tech Stack

* Python 3.12+
* Google Gemini API
* Streamlit
* Wikipedia API
* python-dotenv

---

## 📂 Project Structure

```text
AI-MultiTool-Agent/
│
├── app.py                 # Streamlit frontend
├── agent.py               # Main Agent Loop
├── gemini.py              # Gemini API integration
├── parser.py              # JSON parser
├── prompts.py             # System Prompt
├── tools.py               # Available tools
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── screenshots/
    ├── home.png
    ├── tool_call.png
    └── output.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Santhu14-02/AI-MultiTool-Agent.git
```

```bash
cd AI-MultiTool-Agent
```

---

### Create Virtual Environment

Windows

```bash
py -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

Terminal Version

```bash
py agent.py
```

Streamlit Version

```bash
streamlit run app.py
```

---

## 💡 Example Query

```text
Who is Prabhas?
```

---

## 🔄 Agent Workflow

```text
User Query
      │
      ▼
Gemini Planning
      │
      ▼
Tool Selection
      │
      ▼
Execute Tool
      │
      ▼
Observation
      │
      ▼
Gemini Final Response
```

---

## 🛠️ Available Tools

### 📚 Wikipedia Search

Searches Wikipedia and returns a short summary.

Example:

```text
Who is Ram Charan?
```

---

### 💻 Run Command

Executes system commands.

Example:

```text
Run: dir
```

---

### 🌤️ Weather Tool

Currently implemented as a placeholder.

Future versions will integrate a live weather API.

---

## 📸 Screenshots

### Home Screen

![Home](screenshots/home.png)

---

### Tool Calling Process

![Tool Calling](screenshots/tool_call.png)

---

### Final Output

![Output](screenshots/output.png)

---

## 📌 Sample Output

```text
RAW MODEL OUTPUT

{
 "step":"plan",
 "content":"Search Wikipedia for information about Prabhas."
}

🧠 PLAN

Search Wikipedia for information about Prabhas.

🛠 Calling Tool

wikipedia_search("Prabhas")

👀 OBSERVATION

Prabhas is an Indian actor primarily working in Telugu cinema...

🤖 FINAL ANSWER

Prabhas is an Indian actor who primarily works in Telugu cinema...
```

---

## 🔮 Future Improvements

* 🌦️ Live Weather API integration
* 🌐 Web Search Tool
* 🧮 Calculator Tool
* 📁 File Reader Tool
* 📄 PDF Chat Tool
* 🧠 Memory Support
* 🔍 RAG Integration
* 🗃️ Vector Database Support
* 🤖 Multi-Agent Collaboration
* 🔊 Voice Input & Output

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Ben Max**

Built as part of my Agentic AI learning journey using Python, Google Gemini, and Streamlit.
