# 🤖 Agentic AI with Ollama — Laboratory Exercises

This repository contains my implementation and walkthrough recordings for:

* **LAB 01: LLM API Fundamentals and Multi-turn Context using Ollama**
* **LAB 02A: Agentic Workflow Patterns (Ollama Implementation)**

Each exercise includes:

* ✅ Source code
* 🎥 YouTube demo (unlisted)
* 🧠 Explanation of concepts and implementation

---

# 📘 LAB 01: LLM API Fundamentals

## 🔹 Exercise 1: Multi-turn Context

**Description:**
This exercise demonstrates how multi-turn conversations work using Ollama. The system maintains conversation history using structured messages (`system`, `user`, `assistant`) to simulate a continuous dialogue.

**Key Concepts:**

* Role-based messaging
* Context memory
* Iterative conversation flow

**📂 Code:**
`LAB_01_MultiTurn/multi_turn.py`

**🎥 Demo Video:**
👉 *(Paste your YouTube link here)*

---

# 📗 LAB 02A: Agentic Workflow Patterns

This section demonstrates different **agentic AI patterns** used to structure complex AI workflows.

---

## 🔹 Exercise 1: Prompt Chaining

**Description:**
Breaks a task into sequential steps:

1. Generate outline
2. Expand into draft
3. Polish output

Includes validation and retry mechanism.

**🎥 Demo:**
👉 *(Paste link)*

---

## 🔹 Exercise 2: Routing

**Description:**
Routes user queries to different AI specialists:

* Billing
* Technical
* General
* Feature Request

**Key Idea:** Use classification before responding.

**🎥 Demo:**
👉 *(Paste link)*

---

## 🔹 Exercise 3: Parallelization

**Description:**
Runs multiple AI tasks simultaneously:

* One generates response
* One checks safety

Ensures safe output before returning result.

**🎥 Demo:**
👉 *(Paste link)*

---

## 🔹 Exercise 4: Orchestrator–Workers

**Description:**

* Orchestrator breaks task into sub-questions
* Workers answer in parallel
* Optional second round for deeper analysis
* Final synthesis into report

**🎥 Demo:**
👉 *(Paste link)*

---

## 🔹 Exercise 5: Evaluator–Optimizer

**Description:**

* AI generates output
* Evaluator scores based on:

  * Clarity
  * Accuracy
  * Brevity
* Output is improved iteratively until threshold is met

**🎥 Demo:**
👉 *(Paste link)*

---

## 🔹 Exercise 6: Combined Patterns (Stretch Task)

**Description:**
This integrates all patterns into one pipeline:

1. **Routing** → Select expert (technical/business)
2. **Orchestrator–Workers** → Research in parallel
3. **Synthesis** → Generate draft
4. **Evaluator–Optimizer** → Improve output iteratively

**🎥 Demo:**
👉 *(Paste link)*

---

# 👨‍💻 Submitted by:

**Your Name:** *Josep Melvin L. Arguelles*
**Course:** *MEng PSE*


---
