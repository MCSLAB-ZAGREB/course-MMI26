# Course Policy on Generative AI

## 1. Purpose

ChatGPT and similar tools may be used in this course to support learning, modelling, mathematical analysis, and computation. The objective is not to avoid AI, nor to let AI perform the intellectual work. The objective is to learn how to use an intelligent assistant while retaining control over what should be believed and why.

> **AI may explain, question, criticize, suggest, and help compute. The student must understand, decide, verify, and take responsibility.**

ChatGPT is configured to behave as a modelling mentor. It may ask questions, give partial hints, challenge assumptions, or request an independent attempt instead of immediately providing a finished answer. This is part of the learning design, not a malfunction.

## 2. What is allowed?

Every assessed activity will use one of three simple statuses.

| Status | Meaning | Typical use |
|---|---|---|
| **AI-free** | Generative AI must not be used for the activity | Examinations, quizzes, oral defence, or designated independent work |
| **AI-supported** | The student leads; AI may explain, question, criticize, suggest, check, or help with code | Learning, permitted homework, modelling exercises, project development |
| **AI-integrated** | Substantial co-generation is allowed because evaluating and supervising AI is part of the task | Only activities explicitly marked AI-integrated |

Task-specific instructions take precedence over this general policy. If a graded activity does not state its status, treat it as **AI-free** and ask the instructor before using AI. Private, ungraded study is normally **AI-supported**.

The Project Instructions determine how ChatGPT should behave; they do not grant permission to use it in an assessment.

## 3. Use ChatGPT with a purpose

Before starting, know what you want ChatGPT to do and why that assistance is useful. You do not need to complete a form or follow a rigid prompt template. A short, natural statement is enough.

Four uses are particularly valuable:

### Learn a technique

Ask for explanations, intuition, derivations, analogous examples, or questions that test understanding.

> Explain why a regular perturbation expansion fails in this example. Show one simpler example and then ask me to identify the small parameter.

### Develop a model

Present your initial interpretation and use ChatGPT to expose missing mechanisms, assumptions, scales, alternatives, or failure regimes.

> Here is my proposed cooling model. Critique the assumptions and ask me the two most important questions before I derive the equation.

### Review your work

Ask ChatGPT to inspect a derivation, approximation, model, interpretation, or program without automatically replacing it.

> Check my nondimensionalization. Identify the first consequential error and explain why it matters, but let me correct it.

### Compute

Use ChatGPT to help implement, test, or debug a numerical method after the mathematical model and algorithm are clear.

> Here are the equations and finite-difference scheme. Help me write a readable Python implementation and propose a convergence test.

These labels are optional. ChatGPT should infer the intended use when it is obvious.

## 4. The modelling map

When constructing a model, remain aware of six broad questions:

1. **Purpose and scope:** What must be predicted or decided, why, and within what system boundary?
2. **Quantities and scales:** What quantities, units, data, and characteristic scales matter?
3. **Model construction:** What assumptions, balance laws, constitutive relations, and conditions define the model?
4. **Scaling and regimes:** Which dimensionless parameters and limiting regimes determine what may be neglected?
5. **Solution and verification:** How will the model be solved, and how will the calculation be checked?
6. **Validation and decision:** What evidence and uncertainties determine the justified conclusion and its validity limits?

These are not a checklist that must be answered in every conversation. They are a map for recognizing what stage of modelling is being discussed and what may have been overlooked. A question about a specific technique may require only the parts relevant to that technique.

## 5. A simple working principle

Use the following cycle:

$$
\text{attempt}
\rightarrow \text{AI assistance}
\rightarrow \text{student decision}
\rightarrow \text{independent check}.
$$

In practice:

1. Make a reasonable independent attempt when the task is meant to develop your own reasoning.
2. Ask ChatGPT for a specific kind of help.
3. Decide what to accept, modify, or reject.
4. Check every consequential contribution using evidence appropriate to the claim.

You may ask for a smaller hint, a more direct explanation, an analogous example, an alternative method, or a more critical review. Productive conversation is more important than elaborate prompting.

## 6. What counts as checking?

ChatGPT output is not independent evidence. The check must match the claim.

| AI-assisted contribution | Appropriate checks |
|---|---|
| Algebra or derivation | Reconstruct it, substitute back, and check dimensions and signs |
| Scaling or approximation | Identify the controlling parameter, regime, expected error, and possible breakdown |
| Mathematical model | Check conservation structure, assumptions, constitutive laws, and conditions |
| Numerical result | Use a benchmark, exact or manufactured solution, refinement study, invariant, conservation test, or independent method |
| Technical fact, parameter, or citation | Inspect an appropriate original source, standard, database, or course text |
| Physical prediction or engineering conclusion | Compare with relevant data and consider sensitivity, uncertainty, and model limitations |

Keep the distinction:

$$
\text{verification: did we solve the chosen model correctly?}
$$

$$
\text{validation: is the chosen model adequate for reality and purpose?}
$$

A converged computation may still represent an inadequate physical model.

## 7. Code and numerical simulations

AI may help with code when the activity permits it, but distinguish

$$
\text{physical model}
\neq \text{mathematical model}
\neq \text{algorithm}
\neq \text{code}
\neq \text{computed result}.
$$

You should be able to explain:

- which equations and approximations the code implements;
- which numerical method is used and why;
- the important stability, accuracy, and resolution requirements;
- how the implementation was verified;
- what the computed result does and does not establish.

Prefer understandable reference implementations before unnecessary software complexity or optimization. “The code runs” proves only that one execution terminated without a fatal error.

## 8. Sources

ChatGPT is not a scholarly source and may invent plausible references or facts. Use it to generate search terms or possible leads, then inspect the original material:

$$
\text{AI suggestion}
\rightarrow \text{original source}
\rightarrow \text{inspection}
\rightarrow \text{verified claim}.
$$

Check titles, authors, quotations, DOIs, parameter values, standards, and datasets before using them. Cite the source you inspected, not ChatGPT.

## 9. Disclosure without unnecessary bureaucracy

Disclosure is required when AI materially affects submitted reasoning, mathematics, code, figures, prose, sources, or conclusions. Ordinary spelling and formatting assistance need not be reported unless it changes technical content.

For most assignments, a short declaration is sufficient:

```text
AI USE DECLARATION
Tool:
Purpose: What I asked AI to help with and why.
Contribution used: What materially entered the submission.
My decision: What I accepted, changed, or rejected.
Independent check: How I verified the retained contribution.
```

If no generative AI was used:

```text
AI USE DECLARATION
No generative AI was used in preparing this submission.
```

You do not need to submit complete chat transcripts or log every minor interaction unless the assignment explicitly requests this. For substantial projects, retain enough evidence to explain important AI-influenced decisions.

## 10. Non-negotiable rules

Do not:

- use AI in an AI-free activity;
- conceal material AI assistance;
- submit work that you cannot explain, modify, test, and defend;
- present AI output as verification or as a scientific source;
- retain fabricated citations, data, parameters, quotations, or results;
- use AI to disguise plagiarism or circumvent assessment rules;
- upload confidential, personal, proprietary, unpublished, or restricted material without authorization.

Permission to use AI does not change rules about collaboration, authorship, copyright, or data protection.

## 11. Responsibility and assessment

Intellectual ownership does not require every intermediate sentence or line of code to be produced without assistance. It requires that you can

> **reconstruct, justify, test, modify, and defend every consequential modelling choice.**

Assessment focuses on judgement, reasoning, evidence, verification, interpretation, and communication—not on prompt sophistication. The instructor may ask you to explain a derivation, change a parameter, repair code, compare models, or defend a conclusion without AI.

Unauthorized or undisclosed AI use may be treated as unauthorized assistance under applicable university procedures. Automated AI-detection scores will not be treated as sufficient evidence on their own.

## 12. Before submitting

Ask yourself:

1. What did I ask AI to do, and why?
2. What did I accept, change, or reject?
3. How did I independently check what I retained?
4. Can I explain the assumptions, method, code, limitations, and conclusion?
5. Could I modify or defend the work without ChatGPT?

> **Compact rule:** Use AI deliberately. Keep the decisions yours. Check consequential claims. Disclose material assistance. Remain responsible.
