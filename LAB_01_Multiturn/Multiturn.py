--- FOR 3 TURNS ---

seed_topic = "vector databases in RAG"

messages = [
    {"role": "system", "content": "You are a helpful instructor."}
]

num_turns = 3

messages.append({
    "role": "user",
    "content": f"Generate one strong interview question about {seed_topic}. Return the question only."
})

for turn in range(num_turns):

    response = ollama_client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=messages,
        temperature=1
    )

    assistant_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_content})

    display(Markdown(f"## Turn {turn+1}: Assistant Response\n\n{assistant_content}"))


    if turn == num_turns - 1:
        print("Reached final turn. Stopping without generating new follow-up.")
        break

    if turn == 0:
        user_prompt = "Now answer that question concisely and propose one follow-up question."
    
    elif turn == num_turns - 2:
        user_prompt = "Answer the previous follow-up question concisely. Do NOT generate another follow-up question."
    
    else:
        user_prompt = "Answer the previous follow-up question concisely and propose another follow-up question."

    messages.append({"role": "user", "content": user_prompt})



--- FOR 5 TURNS ---

seed_topic = "vector databases in RAG"

messages = [
    {"role": "system", "content": "You are a helpful instructor."}
]

num_turns = 5

messages.append({
    "role": "user",
    "content": f"Generate one strong interview question about {seed_topic}. Return the question only."
})

for turn in range(num_turns):

    response = ollama_client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=messages,
        temperature=1
    )

    assistant_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_content})

    display(Markdown(f"## Turn {turn+1}: Assistant Response\n\n{assistant_content}"))


    if turn == num_turns - 1:
        print("Reached final turn. Stopping without generating new follow-up.")
        break

    if turn == 0:
        user_prompt = "Now answer that question concisely and propose one follow-up question."
    
    elif turn == num_turns - 2:
        user_prompt = "Answer the previous follow-up question concisely. Do NOT generate another follow-up question."
    
    else:
        user_prompt = "Answer the previous follow-up question concisely and propose another follow-up question."

    messages.append({"role": "user", "content": user_prompt})


--- Without assitant message ---

seed_topic = "vector databases in RAG"

messages = [
    {"role": "system", "content": "You are a helpful instructor."}
]

num_turns = 5

messages.append({
    "role": "user",
    "content": f"Generate one strong interview question about {seed_topic}. Return the question only."
})

for turn in range(num_turns):

    response = ollama_client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=messages,
        temperature=1
    )

    assistant_content = response.choices[0].message.content

    display(Markdown(f"## Turn {turn+1}: Assistant Response\n\n{assistant_content}"))


    if turn == num_turns - 1:
        print("Reached final turn. Stopping without generating new follow-up.")
        break

    if turn == 0:
        user_prompt = "Now answer that question concisely and propose one follow-up question."
    
    elif turn == num_turns - 2:
        user_prompt = "Answer the previous follow-up question concisely. Do NOT generate another follow-up question."
    
    else:
        user_prompt = "Answer the previous follow-up question concisely and propose another follow-up question."

    messages.append({"role": "user", "content": user_prompt})

