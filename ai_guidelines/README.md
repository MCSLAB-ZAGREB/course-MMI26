# Using ChatGPT in Mathematical Modelling in Engineering

This Project helps you become a better mathematical modeller. ChatGPT can teach, guide, question, review, and compute, but it is not an answer service or an authority.

> **AI contributes; you think, act, check, revise, and remain responsible.**

## 1. Set up the Project

For individual learning and assessed work, normally use a **private** Project:

1. Create a Project named **Mathematical Modelling in Engineering**.
2. Paste the whole of **00_CHATGPT_PROJECT_INSTRUCTIONS.md** into Project Instructions. It is about 7,850 characters, just within the 8,000-character limit, so do not add to it; put extra guidance in a source file instead.
3. Add these Project sources:
   - **01_COURSE_CONTEXT.md**, under exactly this name, because the instructions refer to it;
   - the lecture PDFs;
   - the textbook PDF: T. Witelski and M. Bowen, *Methods of Mathematical Modelling: Continuous Systems and Differential Equations* (Springer, 2015);
   - any assessment rules provided by the instructor.
4. Start a separate chat for each substantial task.

| File | Purpose |
|---|---|
| **00_CHATGPT_PROJECT_INSTRUCTIONS.md** | Governs how ChatGPT interacts with you |
| **01_COURSE_CONTEXT.md** | Supplies course scope, weekly schedule, modelling pipeline, notation, conventions, and textbook chapter links |
| **Lecture PDFs** | Give each week's content, terminology, worked examples, and expected level |
| **Textbook PDF** | Adds derivations, alternative approaches, worked examples, and exercises |
| **Assessment rules** (if provided) | State what ChatGPT may and may not do for assessed work |

The textbook PDF must contain searchable text; a scan without a text layer cannot be searched. Use only a copy you are licensed to use. Projects also have a file limit that depends on your plan; if you reach it, merge the lecture PDFs into one file.

Use an instructor-provided setup if directed. Use a shared Project only for intentionally collaborative or common work; do not place individual assessed or sensitive material, or a textbook copy you may not share, there without authorization. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

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

**diagnose → explain → guide → you attempt → review → you revise → synthesis**.

ChatGPT should not immediately complete a target course problem, including a textbook exercise, merely because you request the answer. If you are stuck, help may escalate from a question or hint to a partial derivation, analogous example, guided derivation, and—after meaningful learning—a final synthesis. Direct questions about knowledge should still receive direct explanations.

ChatGPT follows the semester order in **01_COURSE_CONTEXT.md**: it builds on weeks already covered and flags methods from later weeks. When preparing for an exam, say which weeks it covers; the midterm covers Weeks 1–7 and the final the integrated modelling workflow.

Useful prompts include:

- **Teacher:** “Explain the idea using an analogous example, then let me apply it here.”
- **Modelling Mentor:** “Ask me the two most consequential questions before we choose equations.”
- **Critical Reviewer:** “Identify the most consequential weakness, but let me repair it.”
- **Computational Assistant:** “Before writing code, help me predict the result and design an independent check.”

You can also ask ChatGPT to expose assumptions, challenge a scale, compare validity regimes, find a limiting case, or give only the smallest useful next hint. Task instructions may prescribe a role sequence or evidence requirements; follow them.

## 4. Study with the lectures and textbook

The lectures define what each week covers; the textbook deepens it. ChatGPT can connect a lecture, slide, or document you upload in chat to the matching textbook sections, worked examples, and exercises, and tell you where they are.

- Locations are given as chapter, section, example or exercise number, and page. PDF page numbers differ from the printed ones and should be labelled as such.
- The week-to-chapter links in **01_COURSE_CONTEXT.md** are leads to confirm, not a fixed correspondence.
- Where the textbook's notation or scalings differ, ChatGPT maps them onto course conventions, which take precedence.
- Check any cited location yourself before relying on it. If ChatGPT cannot find something, it should say so rather than reconstruct it; paste the relevant excerpt instead.

Useful prompts include:

- “Explain Lecture 5 and point me to the matching textbook sections and exercises.”
- “Map the scaling in this textbook example onto our course notation.”
- “Quiz me on Weeks 3–5, drawing on textbook exercises.”

## 5. Add only relevant material

- Attach an assignment, image, or dataset to its task chat.
- Paste your model, derivation, code, results, and assumptions when requesting feedback.
- Add material as a Project source only when it should be reused across chats.
- Keep unrelated tasks in separate chats.
- Do not upload confidential, proprietary, personal, unpublished, or restricted material without authorization.

## 6. Remain responsible

ChatGPT output is not independent evidence. You must be able to:

- reconstruct the reasoning and identify important assumptions;
- distinguish reality, observations, model, model solution, interpretation, and decision, and likewise the mathematical problem, algorithm, code, and output;
- check units, signs, conditions, limiting cases, sensitivity, stability, convergence, and plausibility as relevant;
- verify computations independently, separate numerical error from model discrepancy, and validate the model against its real purpose;
- inspect original sources for consequential facts, parameters, quotations, citations, and textbook locations;
- explain the validity regime, limitations, and conclusion.

For every result, answer the course questions: What is represented or neglected? Which scales control the regime? Why are the model and method justified? How was the result checked? Where does it fail? What conclusion follows?

**The code runs** does not imply **the solution is correct**: a converged calculation may still solve an inadequate model. ChatGPT should report a number as computed only if it actually ran code; ask if unsure. ChatGPT agreeing with you does not make a claim true.


## Official interface reference

OpenAI's current Projects documentation explains that project instructions apply across project chats, shared files belong in Sources, and task-specific files may be attached to one chat: [Projects and chats](https://learn.chatgpt.com/docs/projects?surface=web).

Nothing about this setup is specific to ChatGPT. The split between Project Instructions (behaviour), Sources (shared reference documents), and chat attachments (task-specific context) has direct equivalents in other assistants — for example, Claude's Projects feature separates custom instructions from project knowledge files in essentially the same way. If the course ever changes tools, these documents should transfer with only minor edits.
