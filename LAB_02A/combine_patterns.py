import json
from concurrent.futures import ThreadPoolExecutor

TOPIC = "How vector databases create business value in AI products"
SCORE_THRESHOLD = 7
MAX_ITERATIONS = 3


CATEGORY_PROMPTS = {
    "technical": "You are a senior technical writer. Be precise and structured.",
    "business":  "You are a business strategist. Focus on value, ROI, and use cases.",
}

def classify_topic(topic: str) -> str:
    result = chat([
        {"role": "system", "content": (
            "Classify the topic as either 'technical' or 'business'. "
            "Reply with one word only."
        )},
        {"role": "user", "content": topic},
    ], temperature=0).strip().lower()

    if "technical" in result:
        return "technical"
    return "business"


def generate_subtasks(topic: str) -> list[str]:
    raw = chat([
        {"role": "system", "content": (
            "You are a research orchestrator. Generate 3–4 focused sub-questions. "
            "Return ONLY JSON array."
        )},
        {"role": "user", "content": topic},
    ], temperature=0)

    clean = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(clean)


def worker_answer(question: str) -> tuple[str, str]:
    answer = chat([
        {"role": "system", "content": "You are a concise expert. Answer in 3–5 sentences."},
        {"role": "user", "content": question},
    ])
    return question, answer


def run_workers(subtasks: list[str]) -> dict:
    with ThreadPoolExecutor(max_workers=len(subtasks)) as pool:
        results = dict(pool.map(lambda q: worker_answer(q), subtasks))
    return results


def synthesize(topic: str, worker_text: str, category: str) -> str:
    system_prompt = CATEGORY_PROMPTS[category]

    return chat([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Topic: {topic}\n\nResearch:\n{worker_text}\n\nWrite a clear 150-word explanation."},
    ])


def evaluate(topic: str, response: str) -> tuple[dict, str]:
    raw = chat([
        {"role": "system", "content": (
            "You are a strict evaluator. Score from 1–10 on clarity, accuracy, brevity. "
            "Return ONLY JSON: {\"clarity\":int,\"accuracy\":int,\"brevity\":int,\"feedback\":\"text\"}"
        )},
        {"role": "user", "content": f"Topic: {topic}\n\nResponse:\n{response}"},
    ], temperature=0)

    clean = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    parsed = json.loads(clean)

    scores = {
        "clarity": int(parsed["clarity"]),
        "accuracy": int(parsed["accuracy"]),
        "brevity": int(parsed["brevity"]),
    }

    return scores, parsed["feedback"]


category = classify_topic(TOPIC)

subtasks = generate_subtasks(TOPIC)

worker_results = run_workers(subtasks)

worker_text = "\n\n".join(f"Q: {q}\nA: {a}" for q, a in worker_results.items())

draft = synthesize(TOPIC, worker_text, category)


feedback = None

for iteration in range(1, MAX_ITERATIONS + 1):
    if iteration > 1:
        draft = chat([
            {"role": "system", "content": CATEGORY_PROMPTS[category]},
            {"role": "user", "content": f"Improve this based on feedback:\n{feedback}\n\n{draft}"}
        ])

    scores, feedback = evaluate(TOPIC, draft)

    display(Markdown(
        f"### Iteration {iteration}\n\n"
        f"Scores: {scores}\n\n"
        f"{draft}\n\n"
        f"Feedback: {feedback}"
    ))

    if all(s >= SCORE_THRESHOLD for s in scores.values()):
        display(Markdown("✅ Final output meets all criteria"))
        break
else:
    display(Markdown("⚠️ Max iterations reached"))
