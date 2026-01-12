def decide_next_step(state: dict) -> str:
    """
    Rule-based branching. No frameworks. No ML classifiers.
    """
    if "skills_extracted" not in state:
        return "extract_skills"
    if "gap_analysis" not in state:
        return "gap_analysis"
    if "improvement_plan" not in state:
        return "improvement_plan"
    if "resume_rewrite" not in state:
        return "resume_rewrite"
    if "self_review" not in state:
        return "self_review"
    return "finish"
