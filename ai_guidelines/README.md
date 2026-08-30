# Using ChatGPT in Mathematical Modelling in Engineering

This Project helps you become a better mathematical modeller. ChatGPT can teach, guide, question, review, and compute, but it is not an answer service or an authority.

> **AI contributes; you think, act, check, revise, and remain responsible.**

## 1. Set up the Project

For individual learning and assessed work, normally use a **private** Project:

1. Create a Project named **Mathematical Modelling in Engineering**.
2. Paste **00_CHATGPT_PROJECT_INSTRUCTIONS.md** into Project Instructions.
3. Add **01_COURSE_CONTEXT.md** as a Project source.
4. Start a separate chat for each substantial task.

| File | Purpose |
|---|---|
| **00_CHATGPT_PROJECT_INSTRUCTIONS.md** | Governs how ChatGPT interacts with you |
| **01_COURSE_CONTEXT.md** | Supplies course scope, methods, notation, and conventions |

Use an instructor-provided setup if directed. Use a shared Project only for intentionally collaborative or common work; do not place individual assessed or sensitive material there without authorization. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## 2. Choose the role

There are no AI levels. The role depends on the intellectual task.

| Role | ChatGPT contributes | You contribute |
|---|---|---|
| **Teacher** | Concepts, reasoning, derivations, hints, or an analogous example | Reconstruct and transfer the method |
| **Modelling Mentor** | Questions and alternatives that expose modelling choices | Choose and justify the model |
| **Critical Reviewer** | Focused criticism of assumptions, mathematics, code, or claims | Judge, revise, and explain |
| **Computational Assistant** | Algorithms, implementation, debugging, experiments, or visualization | Establish the formulation, predict behaviour, and verify |

Name a role if useful; otherwise state your purpose clearly and ChatGPT should infer it.

## 3. Work through the problem

For substantial work, give your objective, available information, current attempt, and point of uncertainty. The interaction should follow an adaptive loop:

**diagnose → guide → you act → check → explain**.

ChatGPT should not immediately complete a target course problem merely because you request the answer. If you are stuck, help may escalate from a question or hint to a partial derivation, analogous example, guided derivation, and—after meaningful learning—a final synthesis. Direct questions about knowledge should still receive direct explanations.

Useful prompts include:

- **Teacher:** “Explain the idea using an analogous example, then let me apply it here.”
- **Modelling Mentor:** “Ask me the two most consequential questions before we choose equations.”
- **Critical Reviewer:** “Identify the most consequential weakness, but let me repair it.”
- **Computational Assistant:** “Before writing code, help me predict the result and design an independent check.”

You can also ask ChatGPT to expose assumptions, challenge a scale, compare validity regimes, find a limiting case, or give only the smallest useful next hint. Task instructions may prescribe a role sequence or evidence requirements; follow them.

## 4. Add only relevant material

- Attach an assignment, image, or dataset to its task chat.
- Paste your model, derivation, code, results, and assumptions when requesting feedback.
- Add material as a Project source only when it should be reused across chats.
- Keep unrelated tasks in separate chats.
- Do not upload confidential, proprietary, personal, unpublished, or restricted material without authorization.

## 5. Remain responsible

ChatGPT output is not independent evidence. You must be able to:

- reconstruct the reasoning and identify important assumptions;
- distinguish the physical system, model, mathematical problem, algorithm, code, and output;
- check units, signs, conditions, limiting cases, sensitivity, stability, convergence, and plausibility as relevant;
- verify computations independently and validate the model against its real purpose;
- inspect original sources for consequential facts, parameters, quotations, and citations;
- explain the validity regime, limitations, and conclusion.

**The code runs** does not imply **the solution is correct**. ChatGPT agreeing with you does not make a claim true.


## Official interface reference

OpenAI's current Projects documentation explains that project instructions apply across project chats, shared files belong in Sources, and task-specific files may be attached to one chat: [Projects and chats](https://learn.chatgpt.com/docs/projects?surface=web).

Nothing about this setup is specific to ChatGPT. The split between Project Instructions (behaviour), Sources (shared reference documents), and chat attachments (task-specific context) has direct equivalents in other assistants — for example, Claude's Projects feature separates custom instructions from project knowledge files in essentially the same way. If the course ever changes tools, these documents should transfer with only minor edits.
