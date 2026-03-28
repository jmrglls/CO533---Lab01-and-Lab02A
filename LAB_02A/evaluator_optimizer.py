WRITING_TASK = "Explain how attention mechanisms work in transformer models, for a junior developer."
SCORE_THRESHOLD = 8
MAX_ITERATIONS  = 4

def generate(task: str, feedback: str | None = None) -> str:
    messages = [
        {"role": "system", "content": "You are a technical educator. Write clearly and concisely (≤150 words)."},
        {"role": "user",   "content": task},
    ]
    if feedback:
        messages.append({"role": "user", "content": f"Improve your previous response based on this feedback:\n{feedback}"})
    return chat(messages)

def evaluate(task: str, response: str) -> tuple[dict, str]:
    """Return (scores_dict, feedback)."""
    raw = chat(
        [
            {"role": "system", "content": (
                "You are a strict writing evaluator. "
                "Score the response from 1–10 on THREE axes: clarity, accuracy, brevity. "
                "Reply ONLY with JSON: "
                "{\"clarity\": <int>, \"accuracy\": <int>, \"brevity\": <int>, \"feedback\": \"<string>\"}"
            )},
            {"role": "user", "content": f"Task: {task}\n\nResponse:\n{response}"},
        ],
        temperature=0,
    ).strip()

    clean = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    parsed = json.loads(clean)

    scores = {
        "clarity": int(parsed["clarity"]),
        "accuracy": int(parsed["accuracy"]),
        "brevity": int(parsed["brevity"]),
    }

    return scores, parsed["feedback"]


feedback = None

for iteration in range(1, MAX_ITERATIONS + 1):
    draft = generate(WRITING_TASK, feedback)
    scores, feedback = evaluate(WRITING_TASK, draft)

    display(Markdown(
        f"### Iteration {iteration}\n\n"
        f"**Scores:** Clarity={scores['clarity']}, Accuracy={scores['accuracy']}, Brevity={scores['brevity']}\n\n"
        f"**Draft:**\n\n{draft}\n\n"
        f"**Evaluator feedback:** {feedback}"
    ))

   
    if all(score >= 7 for score in scores.values()):
        display(Markdown(f"✅ **All thresholds met at iteration {iteration}. Final answer above.**"))
        break
else:
    display(Markdown("⚠️ Max iterations reached without meeting all thresholds."))
