# Setting Up and Using ChatGPT for This Course

ChatGPT is used in this course as a mathematical-modelling mentor: it can explain methods, ask useful questions, criticize assumptions, review mathematics, suggest alternatives, and help with computation. It is not an authority and does not replace your responsibility for the model.

The basic rule is:

> **Use AI deliberately. Keep the decisions yours. Check consequential claims. Disclose material assistance.**

## 1. Create your course Project

1. In ChatGPT, create a new Project.
2. Name it, for example, `Mathematical Modelling in Engineering`.
3. Use this Project for course learning, permitted assignments, and project work.
4. Start a separate chat for each substantial topic or outcome—for example, `Boundary-layer exercise`, `Cooling model review`, or `Project numerical verification`.

A Project keeps its chats, instructions, and shared sources together. A separate chat for each task prevents unrelated arguments, files, and assumptions from becoming mixed.

## 2. Put each item in the correct place

| Item | Where to put it | Purpose |
|---|---|---|
| `00_CHATGPT_PROJECT_INSTRUCTIONS` | Copy its **entire contents** into the Project's **Instructions** or **Project instructions** field | Activates ChatGPT's mentoring behaviour across project chats |
| `00_Course_AI_Policy.md` | Upload to the Project's **Sources** | Makes the course rules available throughout the Project |
| Other instructor-provided course guides and recurring readings | Upload to **Sources** | Provides shared course context across chats |
| One assignment statement, image, dataset, or temporary file | Attach to the relevant **chat** unless it will be reused across several chats | Keeps the shared Project context focused |
| Your derivation, assumptions, code, or results | Paste or attach them in the chat where you want feedback | Allows ChatGPT to review your actual attempt |
| Confidential, personal, proprietary, unpublished, or restricted material | **Do not upload it** without authorization | Protects privacy, intellectual property, and research data |

Do not merely upload `00_CHATGPT_PROJECT_INSTRUCTIONS` as a source. Its contents must be pasted into the active Project Instructions field. Uploading the course policy does not activate the mentoring behaviour, and activating the mentoring behaviour does not give permission to use AI in an assessment.

Interface labels may change slightly. The important distinction is:

- **Project Instructions** control how ChatGPT should behave;
- **Project Sources** provide documents that ChatGPT may consult;
- **chat attachments** provide context needed only for one task.

## 3. Check the assessment status before using AI

Every assessed activity has one of three statuses:

| Status | What it means |
|---|---|
| **AI-free** | Do not use generative AI for the activity. |
| **AI-supported** | You lead the work; AI may explain, question, criticize, suggest, check, or help with code. |
| **AI-integrated** | Substantial co-generation is allowed because supervising and evaluating AI is part of the task. |

Task-specific instructions override the general policy. If a graded activity does not state its status, treat it as **AI-free** and ask the instructor. Private, ungraded study is normally AI-supported.

## 4. Begin with what you need

You do not need elaborate prompts or a compulsory template. State naturally what you are doing, what you have tried, and what kind of help you want.

| What you need | Example opening |
|---|---|
| **Learn a technique** | `Teach me why a regular perturbation expansion fails here. Begin with the small parameter and show one simpler example.` |
| **Develop a model** | `I need to predict the cooling time. Here is my initial system boundary and assumptions. Ask me the two most important questions before we write equations.` |
| **Review your work** | `Check my nondimensionalization. Identify the first consequential error, explain why it matters, and let me correct it.` |
| **Compute** | `Here are my equations and finite-difference scheme. Help me produce readable Python code and design a convergence test.` |

You may name the mode, but this is optional. Useful requests include:

- `Give me only a hint.`
- `Ask one question at a time.`
- `This is technique learning, not a modelling exercise; explain the method directly.`
- `Review my work without rewriting it.`
- `Show an analogous example, then let me solve this one.`
- `Summarize what I have decided and what remains unverified.`
- `Now give the next step and explain why it is valid.`

ChatGPT may ask for your attempt, question an assumption, or decline to provide a complete assigned solution. That behaviour is intentional. The aim is to improve your ability to formulate and defend the next step without AI.

## 5. Use the modelling map when it is relevant

For a modelling problem, remain aware of six broad questions:

1. **Purpose and scope:** What must be predicted or decided, why, and within what system boundary?
2. **Quantities and scales:** What quantities, units, data, and characteristic scales matter?
3. **Model construction:** What assumptions, balance laws, constitutive relations, and conditions define the model?
4. **Scaling and regimes:** Which dimensionless parameters and limiting regimes determine what may be neglected?
5. **Solution and verification:** How will the model be solved, and how will the calculation be checked?
6. **Validation and decision:** What evidence and uncertainties determine the justified conclusion and its validity limits?

These questions are a map, not a form. You do not need to answer all six in every message. ChatGPT should infer what is already known and ask only the next useful question.

If you are learning a specific mathematical technique—such as perturbation theory, boundary layers, multiple scales, or Fourier methods—only the relevant questions apply. For asymptotic analysis, the important issues may instead be the small parameter, ordering, dominant balance, regular or singular character, uniform validity, breakdown, matching, and error.

## 6. Follow a simple learning cycle

Use ChatGPT through the cycle

$$
\text{attempt}
\rightarrow \text{AI assistance}
\rightarrow \text{your decision}
\rightarrow \text{independent check}.
$$

An independent attempt need not be long. It may be a proposed system boundary, a sketch of the dominant balance, one line of a derivation, pseudocode, or an explanation of where you are stuck. The purpose is to make your reasoning visible before AI suggestions anchor the solution.

After receiving help, decide explicitly what to accept, modify, or reject. ChatGPT output is a candidate explanation, equation, model, or implementation—not evidence that it is correct.

## 7. Check different claims in different ways

| Contribution | Appropriate independent check |
|---|---|
| Algebra or derivation | Reconstruct it, substitute back, and inspect dimensions and signs |
| Scaling or approximation | Identify the controlling parameter, validity regime, expected error, and breakdown |
| Mathematical model | Examine conservation, assumptions, closures, and initial, boundary, or interface conditions |
| Numerical result | Use a benchmark, exact or manufactured solution, refinement study, invariant, conservation test, or independent method |
| Technical fact, parameter, or citation | Inspect the original source, standard, database, or course text |
| Physical prediction or engineering conclusion | Compare with relevant data and examine sensitivity, uncertainty, and model limitations |

Remember:

$$
\text{verification asks whether the chosen model was solved correctly,}
$$

$$
\text{validation asks whether the model is adequate for reality and purpose.}
$$

AI cannot serve as independent verification of its own output.

## 8. Use ChatGPT for numerical work without hiding the mathematics

Before requesting code, establish the mathematical problem, numerical method, expected behaviour, and at least one verification test. Keep distinct:

$$
\text{physical model}
\neq \text{mathematical model}
\neq \text{algorithm}
\neq \text{code}
\neq \text{computed result}.
$$

Unless the task requires something else, ask first for a transparent reference implementation:

- ordinary Python with NumPy, SciPy, and Matplotlib;
- `scipy.integrate.solve_ivp` for suitable ODE initial-value problems;
- `scipy.integrate.solve_bvp` for suitable two-point boundary-value problems;
- finite differences for initial PDE prototypes;
- FDTD for suitable time-domain wave or electromagnetic problems.

Use NGSolve, FEniCSx, BEM packages, PETSc, or other specialized software only when the assignment requires it, you request it, or there is a clear technical reason. Begin with a readable serial baseline. Discuss vectorization, sparse methods, JIT compilation, GPUs, MPI, domain decomposition, or other HPC improvements only after the baseline is understood and verified.

You must be able to explain what equations the program represents, what discretization it uses, its stability and resolution requirements, how it was verified, and what its output does and does not establish. “The code runs” is not a verification result.

## 9. Use sources correctly

ChatGPT is not a scholarly source. It may invent references, quotations, data, or parameter values. Use AI-generated citations only as search leads:

$$
\text{AI suggestion}
\rightarrow \text{original source}
\rightarrow \text{inspection}
\rightarrow \text{verified claim}.
$$

Cite the source you actually inspected, not ChatGPT.

## 10. Disclose material assistance briefly

When AI materially affects submitted reasoning, mathematics, code, figures, prose, sources, or conclusions, include the declaration required by the course policy:

```text
AI USE DECLARATION
Tool:
Purpose: What I asked AI to help with and why.
Contribution used: What materially entered the submission.
My decision: What I accepted, changed, or rejected.
Independent check: How I verified the retained contribution.
```

You do not need to log every minor interaction or submit complete transcripts unless an assignment explicitly requests them. Retain enough evidence to explain important AI-influenced decisions.

## 11. Before submitting

Ask yourself:

1. What did I ask AI to do, and why?
2. What did I accept, change, or reject?
3. How did I independently check what I retained?
4. Can I explain the assumptions, method, code, limitations, and conclusion?
5. Could I modify or defend the work without ChatGPT?

You own the work only if you can reconstruct, justify, test, modify, and defend every consequential modelling choice.

## Official interface reference

OpenAI's current Projects documentation explains that project instructions apply across project chats, shared files belong in Sources, and task-specific files may be attached to one chat: [Projects and chats](https://learn.chatgpt.com/docs/projects?surface=web).
