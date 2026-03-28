RESEARCH_GOAL = "Explain how Retrieval-Augmented Generation (RAG) works and when to use it."

plan_raw = chat(
    [
        {"role": "system", "content": (
            "You are a research orchestrator. Given a goal, output a JSON array of 3–4 "
            "focused sub-questions to investigate. Return ONLY valid JSON, no other text."
        )},
        {"role": "user", "content": RESEARCH_GOAL},
    ],
    temperature=0,
)

plan_clean = plan_raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
subtasks: list[str] = json.loads(plan_clean)

display(Markdown("### Orchestrator Plan\n\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(subtasks))))

def worker_answer(question: str) -> tuple[str, str]:
    answer = chat([
        {"role": "system", "content": "You are a concise AI/ML expert. Answer in 3–5 sentences."},
        {"role": "user",   "content": question},
    ])
    return question, answer

with ThreadPoolExecutor(max_workers=len(subtasks)) as pool:
    worker_results = dict(pool.map(lambda q: worker_answer(q), subtasks))

worker_text = "\n\n".join(f"**Q: {q}**\n\n{a}" for q, a in worker_results.items())
display(Markdown("### Worker Answers (Round 1)\n\n" + worker_text))


decision = chat([
    {"role": "system", "content": (
        "You are a research evaluator. Decide if the answers need deeper follow-up questions. "
        "Reply ONLY with 'yes' or 'no'."
    )},
    {"role": "user", "content": worker_text},
], temperature=0).strip().lower()


worker_text_round2 = ""

if decision == "yes":
    display(Markdown("### 🔁 Second Round Triggered"))

    plan2_raw = chat([
        {"role": "system", "content": (
            "You are a research orchestrator. Based on the previous answers, "
            "generate 2–3 deeper follow-up questions. Return ONLY JSON."
        )},
        {"role": "user", "content": worker_text},
    ], temperature=0)

    plan2_clean = plan2_raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    subtasks2: list[str] = json.loads(plan2_clean)

    with ThreadPoolExecutor(max_workers=len(subtasks2)) as pool:
        worker_results2 = dict(pool.map(lambda q: worker_answer(q), subtasks2))

    worker_text_round2 = "\n\n".join(f"**Q: {q}**\n\n{a}" for q, a in worker_results2.items())
    display(Markdown("### Worker Answers (Round 2)\n\n" + worker_text_round2))

else:
    display(Markdown("### ✅ No Second Round Needed"))


final_input = f"Goal: {RESEARCH_GOAL}\n\nRound 1:\n{worker_text}"

if worker_text_round2:
    final_input += f"\n\nRound 2:\n{worker_text_round2}"

final_report = chat([
    {"role": "system", "content": "You are a senior technical writer. Synthesise into a structured report (~200 words)."},
    {"role": "user",   "content": final_input},
])

display(Markdown("### Final Synthesised Report\n\n" + final_report))
