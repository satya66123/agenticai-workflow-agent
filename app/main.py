import json
import time
from pathlib import Path

from app.models import AgentInput
from app.llm_client import call_llm


SYSTEM = """
You are an autonomous workflow agent.

Given Resume Text and Job Description, do ALL in ONE response:
1) Extract skills
2) Skill gap analysis
3) 30-day plan
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


def load_example(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def main():
    start = time.time()

    resume = load_example("examples/resume.txt").strip()[:3000]  # ✅ trim for speed
    jd = load_example("examples/job_description.txt").strip()[:2500]

    # ✅ validation check
    _ = AgentInput(resume_text=resume, job_description=jd)

    prompt = f"""
Resume:
{resume}

Job Description:
{jd}
"""

    raw = call_llm(SYSTEM, prompt)

    # Try parsing JSON (if valid JSON)
    try:
        output = json.loads(raw)
    except Exception:
        output = {"raw": raw}

    Path("runs").mkdir(exist_ok=True)
    Path("runs/final_run.json").write_text(json.dumps(output, indent=2), encoding="utf-8")

    end = time.time()
    print("✅ Agent run completed. Output saved to runs/final_run.json")
    print(f"⚡ Time taken: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
