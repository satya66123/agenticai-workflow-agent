from app.decision_engine import decide_next_step


def test_decision_extract_skills_first():
    state = {}
    assert decide_next_step(state) == "extract_skills"


def test_decision_gap_analysis_after_skills():
    state = {"skills_extracted": {"raw": "dummy"}}
    assert decide_next_step(state) == "gap_analysis"


def test_decision_improvement_plan_after_gap():
    state = {
        "skills_extracted": {"raw": "dummy"},
        "gap_analysis": {"raw": "dummy"}
    }
    assert decide_next_step(state) == "improvement_plan"


def test_decision_resume_rewrite_after_plan():
    state = {
        "skills_extracted": {"raw": "dummy"},
        "gap_analysis": {"raw": "dummy"},
        "improvement_plan": {"raw": "dummy"}
    }
    assert decide_next_step(state) == "resume_rewrite"


def test_decision_self_review_after_rewrite():
    state = {
        "skills_extracted": {"raw": "dummy"},
        "gap_analysis": {"raw": "dummy"},
        "improvement_plan": {"raw": "dummy"},
        "resume_rewrite": {"raw": "dummy"}
    }
    assert decide_next_step(state) == "self_review"


def test_decision_finish():
    state = {
        "skills_extracted": {"raw": "dummy"},
        "gap_analysis": {"raw": "dummy"},
        "improvement_plan": {"raw": "dummy"},
        "resume_rewrite": {"raw": "dummy"},
        "self_review": {"raw": "dummy"}
    }
    assert decide_next_step(state) == "finish"
