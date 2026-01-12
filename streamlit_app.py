import json
import time
from pathlib import Path

import streamlit as st

from app.models import AgentInput
from app.llm_client import call_llm


SYSTEM = """
You are an autonomous workflow agent.

Given Resume Text and Job Description, do ALL in ONE response:
1) Extract skills
2) Skill gap analysis
3) 30-day improvement plan
4) Rewrite resume summary + 5 bullets
5) Self review + refine

Return STRICT JSON ONLY in this format:
{
  "skills_extracted": { "resume_skills": [...], "jd_skills": [...] },
  "gap_analysis": { "missing_skills": [...], "weak_skills": [...], "strong_skills": [...] },
  "improvement_plan": { "priority_skills": [...], "plan": [...], "projects": [...] },
  "resume_rewrite": { "summary": "...", "bullets": [...] },
  "self_review": { "final_summary": "...", "final_bullets": [...], "notes": "..." }
}
"""


def trim_text(text: str, limit: int) -> str:
    return text.strip()[:limit]


st.set_page_config(page_title="Agentic Workflow Agent", layout="wide")

st.title("🤖 Agentic AI Project 2 — Workflow Agent")
st.caption("Resume → JD → Skill Gap → Plan → Rewrite → Self-Review (One-shot fast execution)")

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("📄 Resume Text", height=320, placeholder="Paste your resume here...")

with col2:
    jd_text = st.text_area("🧾 Job Description", height=320, placeholder="Paste job description here...")

st.markdown("---")

colA, colB, colC = st.columns([1, 1, 2])

with colA:
    resume_limit = st.number_input("Resume Limit (chars)", min_value=500, max_value=10000, value=3000, step=250)

with colB:
    jd_limit = st.number_input("JD Limit (chars)", min_value=500, max_value=10000, value=2500, step=250)

with colC:
    run_btn = st.button("🚀 Run Agent", use_container_width=True)

if run_btn:
    if len(resume_text.strip()) < 50 or len(jd_text.strip()) < 50:
        st.error("❌ Please enter valid Resume & Job Description (minimum 50 characters).")
        st.stop()

    start = time.time()

    resume_trimmed = trim_text(resume_text, int(resume_limit))
    jd_trimmed = trim_text(jd_text, int(jd_limit))

    # Validate input
    _ = AgentInput(resume_text=resume_trimmed, job_description=jd_trimmed)

    prompt = f"""
Resume:
{resume_trimmed}

Job Description:
{jd_trimmed}
"""

    with st.spinner("Running autonomous workflow..."):
        raw = call_llm(SYSTEM, prompt)

    # Parse JSON
    try:
        output = json.loads(raw)
        st.success("✅ Agent output generated successfully!")
    except Exception:
        output = {"raw": raw}
        st.warning("⚠️ Model returned non-JSON output. Saved raw response.")

    # Save outputs
    Path("runs").mkdir(exist_ok=True)
    out_path = Path("runs/streamlit_run.json")
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")

    end = time.time()
    st.info(f"⚡ Time taken: {end - start:.2f} seconds")

    # UI Output
    st.subheader("📌 Final Output JSON")
    st.json(output)

    st.download_button(
        "⬇️ Download JSON Report",
        data=json.dumps(output, indent=2, ensure_ascii=False),
        file_name="agentic_workflow_report.json",
        mime="application/json",
        use_container_width=True,
    )

    st.caption(f"Saved locally: `{out_path}`")
