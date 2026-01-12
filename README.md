# 🤖 Agentic AI Project 2 — Workflow Agent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-ff4b4b)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-black)](https://platform.openai.com/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Autonomous workflow agent** that performs:  
> **Resume → JD → Skill Gap → Plan → Rewrite → Self-Review**  
> with **structured JSON output** + **Streamlit UI** + **downloadable report**.

---

## ✨ Repo About (GitHub "About" Section)

**Description (One line):**  
Production-style agentic workflow app that analyzes Resume + JD, identifies skill gaps, generates an improvement plan, rewrites resume content, and self-reviews output.

**Website (optional):**  
`http://localhost:8501` (Streamlit local demo)

---

## 🏷️ GitHub Topics / Tags

Copy & paste into GitHub → **Settings → Topics**

agentic-ai
autonomous-agent
workflow-agent
ai-agent
llm
openai
prompt-engineering
structured-output
state-machine
resume-analyzer
job-description-analyzer
career-assistant
python
pydantic
streamlit
json
portfolio-project

yaml
Copy code

---

## 📌 Overview

**Agentic AI Project 2 — Workflow Agent** is a lightweight, recruiter-ready AI project that demonstrates **autonomous workflow execution** using LLM orchestration.

This agent takes:
- ✅ Resume Text
- ✅ Job Description Text

And produces:
- ✅ extracted skills
- ✅ skill gap analysis
- ✅ improvement plan
- ✅ rewritten resume summary + bullets
- ✅ self-review refinement

All outputs are returned as **strict JSON**, displayed in **Streamlit UI**, and can be downloaded as a report.

---

## 🎯 Key Highlights

✅ Autonomous workflow style reasoning  
✅ Multi-stage output generation (agentic pipeline)  
✅ One-shot execution mode for speed (~15–20 seconds)  
✅ Strict JSON output (excellent for integrations)  
✅ Streamlit UI for user-friendly demo  
✅ Download report button (JSON file)  

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **OpenAI API**
- **Pydantic** (request validation)
- **Streamlit** (UI)
- JSON reporting

---

## 🧠 Workflow

**Workflow Type:**  
✅ Resume → JD → Skill Gap → Plan → Rewrite → Self-Review

The agent returns output in the format:

```json
{
  "skills_extracted": { "resume_skills": [], "jd_skills": [] },
  "gap_analysis": { "missing_skills": [], "weak_skills": [], "strong_skills": [] },
  "improvement_plan": { "priority_skills": [], "plan": [], "projects": [] },
  "resume_rewrite": { "summary": "", "bullets": [] },
  "self_review": { "final_summary": "", "final_bullets": [], "notes": "" }
}
📂 Project Structure
lua
Copy code
agentic-workflow-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── llm_client.py
│   ├── workflow.py
│   └── utils.py
│
├── examples/
│   ├── resume.txt
│   └── job_description.txt
│
├── runs/
│   ├── final_run.json
│   └── streamlit_run.json
│
├── streamlit_app.py
├── planner.md
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
🔑 Setup Instructions
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/agentic-workflow-agent.git
cd agentic-workflow-agent
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv .venv
Activate:

Windows

bash
Copy code
.venv\Scripts\activate
Linux / Mac

bash
Copy code
source .venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add .env File
Create .env in the project root:

env
Copy code
OPENAI_API_KEY=your_openai_key_here
MODEL_NAME=gpt-4o-mini
✅ gpt-4o-mini is recommended for best speed & cost.

▶️ Run in CLI Mode
This runs the agent from terminal:

bash
Copy code
python -m app.main
✅ Output generated here:

bash
Copy code
runs/final_run.json
🖥️ Run Streamlit UI
Start the Streamlit app:

bash
Copy code
streamlit run streamlit_app.py
Open browser:

arduino
Copy code
http://localhost:8501
✅ Features:

Paste Resume Text

Paste Job Description

Limit input size (chars)

Click Run Agent

View JSON output

Download JSON Report

Output also saved locally in /runs

Generated file:

bash
Copy code
runs/streamlit_run.json
⏱️ Performance
Typical runtime:

~15–20 seconds

depends on:

resume length

JD length

internet latency

✅ One-shot execution drastically reduces runtime compared to multi-call pipelines.

✅ Sample Output (Example)
Example keys produced:

skills_extracted.resume_skills

skills_extracted.jd_skills

gap_analysis.missing_skills

improvement_plan.plan

resume_rewrite.summary

self_review.final_bullets

🔒 Design Constraints (Intentional)
This repo intentionally avoids:

❌ RAG

❌ embeddings

❌ vector databases

❌ LangChain / CrewAI frameworks

Reason: keep it simple, lightweight, and purely focused on agentic workflow design.

📜 License
This project is licensed under the MIT License.
See: LICENSE

👤 Author
Satya Srinath
GitHub: @satya66123
Email: satyasrinath653512@gmail.com

yaml
Copy code

---

## ✅ Additional: GitHub Repository Settings (Copy Paste)

### ✅ Repo Name
agentic-workflow-agent

shell
Copy code

### ✅ Repo Description
Autonomous workflow agent: Resume → JD → Skill Gap → Plan → Rewrite → Self-Review with Streamlit UI + structured JSON output.


### ✅ Status: completed ✅✅✅✅✅✅✅


---

## 🚀 Future Updates (Roadmap)

Planned improvements for upcoming versions:

- ✅ Add session-based history tracking (store multiple runs with timestamps)
- ✅ Export report in multiple formats (JSON + TXT + Markdown)
- ✅ Add "Copy Output" button in Streamlit UI
- ✅ Add input upload option (Upload Resume/JD as `.txt` file)
- ✅ Add token usage tracking (input tokens + output tokens)
- ✅ Improve skill gap scoring (priority weights for missing skills)
- ✅ Add resume ATS optimization mode (ATS-friendly summary + keyword mapping)
- ✅ Add evaluation scoring (output quality score & feedback)
- ✅ Optional caching to reduce repeat API costs

These upgrades will make the agent more scalable, production-ready, and better suited for real-world deployment.
