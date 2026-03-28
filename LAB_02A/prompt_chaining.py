import re
def is_valid_outline(outline: str) -> bool:
    lines = [line.strip() for line in outline.strip().split("\n") if line.strip()]
    
    if len(lines) != 3:
        return False
    
    pattern = r"^[1-3]\.\s.+$"
    
    for i, line in enumerate(lines):
        if not re.match(pattern, line):
            return False
        if not line.startswith(f"{i+1}."):
            return False
    
    return True

TOPIC = "Why vector databases matter for RAG applications"


max_retries = 2
attempt = 0
outline = None

while attempt <= max_retries:
    attempt += 1
    
    outline = chat([
        {"role": "system", "content": "You are a technical content strategist."},
        {"role": "user", "content": f"""Write a 3-section outline for a blog post about: {TOPIC}.

STRICT FORMAT:
1. Title
2. Title
3. Title

Return ONLY the outline. No explanations.
"""}
    ])
    
    display(Markdown("### Step 1 — Outline\n\n" + outline))
    
    if is_valid_outline(outline):
        print(f"\n✅ Passed on attempt {attempt}")
        break
    else:
        print("❌ Invalid format, retrying...")


if not is_valid_outline(outline):
    raise ValueError("Failed to generate valid outline after retries.")


draft = chat([
    {"role": "system",    "content": "You are a senior technical writer."},
    {"role": "user",      "content": f"Topic: {TOPIC}"},
    {"role": "assistant", "content": outline},
    {"role": "user",      "content": "Expand the outline into a concise 200-word blog post draft."},
])
display(Markdown("### Step 2 — Draft\n\n" + draft))

polished = chat([
    {"role": "system", "content": "You are an editor who simplifies technical writing."},
    {"role": "user",   "content": f"Rewrite the following blog post so it is engaging for a non-technical audience. Keep it under 150 words.\n\n{draft}"},
])
display(Markdown("### Step 3 — Polished\n\n" + polished))
