SPECIALIST_PROMPTS = {
    "billing":   "You are a billing support specialist. Be empathetic and solution-focused.",
    "technical": "You are a senior technical support engineer. Give precise, step-by-step answers.",
    "general":   "You are a friendly customer success agent. Be warm and concise.",
    "feature_request": "You are a product manager. Acknowledge the request, ask clarifying questions if needed, and explain how it might be evaluated or prioritized.",
}

def classify_query(user_query: str) -> str:
    """Return one of: billing | technical | general | feature_request"""
    result = chat(
        [
            {"role": "system", "content": (
                "Classify the following customer query into exactly one category: "
                "billing, technical, general or feature_request. "
                "Reply with the single word only."
            )},
            {"role": "user", "content": user_query},
        ],
        temperature=0,
    ).strip().lower()
   
    if result in SPECIALIST_PROMPTS:
        return result
    return "general"

def routed_response(user_query: str) -> str:
    category = classify_query(user_query)
    system_prompt = SPECIALIST_PROMPTS[category]
    answer = chat([
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_query},
    ])
    return category, answer

queries = [
    "I was charged twice on my last invoice.",
    "My API requests keep returning a 429 error even though I'm below the limit.",
    "What are your business hours?",
    "I wish your app had dark mode.",
    "Can you add export to PDF feature in the dashboard?",
]

for q in queries:
    category, answer = routed_response(q)
    display(Markdown(f"**Query:** {q}\n\n**Routed to:** `{category}`\n\n**Response:** {answer}\n\n---"))
