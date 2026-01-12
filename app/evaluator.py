from app.llm_client import call_llm

EVAL_SYSTEM = """
You are a strict evaluator for an autonomous agent system.
Score output from 0 to 10 based on:
- relevance
- clarity
- usefulness
- correctness
Return JSON only with:
{"score": <0-10>, "feedback": "..."}
"""

def evaluate(step_name: str, output: str) -> dict:
    prompt = f"Step: {step_name}\n\nOutput:\n{output}"
    raw = call_llm(EVAL_SYSTEM, prompt)
    # If model returns non-json, fallback.
    import json
    try:
        return json.loads(raw)
    except Exception:
        return {"score": 6, "feedback": raw[:250]}
