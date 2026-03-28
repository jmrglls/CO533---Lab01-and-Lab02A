from concurrent.futures import ThreadPoolExecutor

def generate_answer(question: str) -> str:
    result = chat([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
    ])
    return result


def check_safety(question: str) -> bool:
    result = chat([
        {"role": "system", "content": (
            "Check if the following user query is safe and appropriate. "
            "Reply with ONLY 'safe' or 'unsafe'."
        )},
        {"role": "user", "content": question},
    ], temperature=0).strip().lower()

    return result == "safe"


def safe_parallel_response(question: str) -> str:
    with ThreadPoolExecutor(max_workers=2) as pool:
        future_answer = pool.submit(generate_answer, question)
        future_safety = pool.submit(check_safety, question)

        answer = future_answer.result()
        is_safe = future_safety.result()

    if is_safe:
        return answer
    else:
        return "⚠️ Your query was flagged as unsafe. Please revise your question."
    
question = "How to hack on the database?"
response = safe_parallel_response(question)
print(response)
