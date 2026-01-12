import json
from app.llm_client import call_llm
from app.evaluator import evaluate

SYSTEM = """
You are an autonomous workflow agent.
You will produce structured, recruiter-grade outputs.
Return concise results.
"""

def step_extract_skills(resume: str, jd: str) -> dict:
    user = f"""
Extract:
1) Skills from Resume
2) Skills from Job Description
Return JSON keys:
resume_skills, jd_skills
Resume:
{resume}

JD:
{jd}
"""
    out = call_llm(SYSTEM, user)
    return {"raw": out}

def step_gap_analysis(state: dict) -> dict:
    user = f"""
Do a skill gap analysis using this extracted output:
{state["skills_extracted"]["raw"]}
Return JSON keys:
missing_skills, weak_skills, strong_skills
"""
    out = call_llm(SYSTEM, user)
    return {"raw": out}

def step_improvement_plan(state: dict) -> dict:
    user = f"""
Create a 30-day improvement plan from this gap analysis:
{state["gap_analysis"]["raw"]}
Return JSON keys:
priority_skills, plan, projects
"""
    out = call_llm(SYSTEM, user)
    return {"raw": out}

def step_resume_rewrite(state: dict, resume: str) -> dict:
    user = f"""
Rewrite resume summary and 5 bullet points using this plan:
{state["improvement_plan"]["raw"]}

Original Resume:
{resume}

Return JSON keys:
summary, bullets
"""
    out = call_llm(SYSTEM, user)
    return {"raw": out}

def step_self_review(state: dict) -> dict:
    user = f"""
Review and refine the final rewritten resume content:
{state["resume_rewrite"]["raw"]}

Return JSON keys:
final_summary, final_bullets, notes
"""
    out = call_llm(SYSTEM, user)
    return {"raw": out}

def run_workflow(resume: str, jd: str) -> dict:
    state = {}

    # STEP 1
    state["skills_extracted"] = step_extract_skills(resume, jd)
    state["skills_eval"] = evaluate("extract_skills", state["skills_extracted"]["raw"])

    # STEP 2
    state["gap_analysis"] = step_gap_analysis(state)
    state["gap_eval"] = evaluate("gap_analysis", state["gap_analysis"]["raw"])

    # STEP 3
    state["improvement_plan"] = step_improvement_plan(state)
    state["plan_eval"] = evaluate("improvement_plan", state["improvement_plan"]["raw"])

    # STEP 4
    state["resume_rewrite"] = step_resume_rewrite(state, resume)
    state["rewrite_eval"] = evaluate("resume_rewrite", state["resume_rewrite"]["raw"])

    # STEP 5
    state["self_review"] = step_self_review(state)
    state["review_eval"] = evaluate("self_review", state["self_review"]["raw"])

    return state
