---
title: "Course Policy on Generative AI"
subtitle: "Mathematical Modelling in Engineering"
date: "Academic year 2026/2027"
version: "1.0 — 30 August 2026"
lang: en
---

# Course Policy on Generative AI

## 1. Purpose

Generative-AI tools may support learning in **Mathematical Modelling in Engineering**, but they do not replace modelling judgement, mathematical understanding, independent verification, or student responsibility.

The governing principle is:

> **AI may propose; the student must decide, justify, verify, and defend.**

This course treats modelling as the chain

$$
\text{engineering situation}
\rightarrow \text{question}
\rightarrow \text{system boundary}
\rightarrow \text{variables and scales}
\rightarrow \text{assumptions}
\rightarrow \text{balance and constitutive laws}
\rightarrow \text{equations and data}
\rightarrow \text{approximation}
\rightarrow \text{solution}
\rightarrow \text{verification and validation}
\rightarrow \text{interpretation}
\rightarrow \text{engineering decision}.
$$

AI can assist at selected stages of this chain. It is never the epistemic authority that determines whether a model or conclusion should be believed.

## 2. Scope and precedence

This policy applies to ChatGPT and comparable generative systems, including conversational assistants, AI search summaries, generative coding assistants, and generative features embedded in writing, mathematical, or programming software.

Ordinary calculators, conventional numerical or symbolic software, reference managers, and non-generative spelling tools are not automatically treated as generative AI. Their use may nevertheless be restricted by an individual assessment.

The following order of precedence applies:

1. University and faculty regulations on academic integrity, privacy, copyright, and assessment.
2. Written instructions for the particular assessment or task.
3. This course policy.

An assessment may permit less AI assistance than this general policy. When the permitted level is not stated, the defaults in Section 4 apply. If uncertainty remains, the student must ask before using AI.

## 3. AI autonomy levels

Each course activity may be assigned a maximum AI level. A higher level normally includes the lower levels unless the task instructions state otherwise.

| Level | Role of AI | Typical permitted use |
|---|---|---|
| **AI-0** | No AI | Independent work without generative-AI assistance |
| **AI-1** | Explanation | Clarify terminology or explain a concept after an independent attempt |
| **AI-2** | Criticism | Identify possible errors, missing assumptions, or failure modes in student-produced work |
| **AI-3** | Suggestion | Propose alternative models, scales, experiments, solution methods, or checks |
| **AI-4** | Mathematical assistance | Check algebra, derivations, nondimensionalization, asymptotics, or analytical calculations |
| **AI-5** | Code assistance | Suggest, generate, explain, test, or debug code under student supervision |
| **AI-6** | Co-generation | Contribute substantially to an integrated solution when this is explicitly authorized and fully disclosed |
| **AI-7** | Autonomous solution | Produce the task substantially from start to finish with little student control; normally prohibited |

The assigned level is a **maximum permission, not a learning objective**. More AI autonomy is not automatically better. The relevant skill is knowing when assistance is useful and when it destroys independent reasoning or control.

## 4. Default rules by activity

| Activity | Default maximum | Course rule |
|---|---:|---|
| Private, ungraded study | **AI-2** | Make an independent attempt first; use AI mainly for explanation and criticism |
| In-class modelling studio or exercise | As announced | Follow the level stated for each phase of the activity |
| Homework or other graded submission | **AI-0 if unspecified** | Use only the level stated in the written task instructions |
| Computational laboratory | As announced, often **AI-5** | Specify the algorithm before coding and verify the implementation independently |
| Semester project: initial problem formulation | **AI-0** | Define the question, boundary, quantities of interest, variables, mechanisms, assumptions, and required data independently |
| Semester project: critique and alternatives | **AI-2–AI-3** | AI may enlarge the candidate-model space; the student selects and justifies the model |
| Semester project: analysis and implementation | **AI-4–AI-5** when authorized | All consequential mathematics and code must be understood, tested, and disclosed |
| Semester project: integrated co-generation | **AI-6 only when explicitly stated** | Requires process evidence, an AI-use declaration, and oral defence |
| First draft of the final scientific interpretation | **AI-0** | Interpret results independently before editorial AI assistance is considered |
| Short quizzes and independent checkpoints | **AI-0** | No generative-AI assistance |
| Midterm examination | **AI-0** | No generative-AI assistance |
| Final written examination | **AI-0** | No generative-AI assistance |
| Oral defence or viva | **AI-0** | The student must reason and respond independently |

During an AI-0 activity, AI-generated notes, answers, code, or summaries may not be consulted unless the instructor explicitly supplies them as part of the task.

## 5. Progressive use during the semester

AI is integrated into the modelling curriculum only after students establish an independent baseline.

| Course phase | Normal role of AI | Required human contribution |
|---|---|---|
| Weeks 1–2: dimensions, scales, nondimensionalization | Critic after an independent attempt | Choose variables, units, characteristic scales, and final dimensionless groups |
| Weeks 3–6: dominant balance and asymptotics | Critic and mathematical checker | Identify the perturbation structure, distinguished limits, and breakdown regimes |
| Week 7: conservation and constitutive laws | Hostile reviewer | Derive the initial balance and identify closure assumptions independently |
| Week 8: midterm | None | Demonstrate unaided modelling capability |
| Weeks 9–12: transport, Fourier methods, fundamental solutions, multiscale models | Critic, alternative generator, mathematical or code assistant as assigned | Justify constitutive laws, boundary conditions, scales, approximations, and interpretation |
| Weeks 13–14: industrial modelling | Disclosed integrated assistance may be permitted | Retain decision authority, verification evidence, uncertainty analysis, and defensible conclusions |
| Week 15: final examination | None | Demonstrate integrated unaided modelling capability |

## 6. Required AI-assisted workflow

When AI use is permitted, students must follow this sequence:

1. **Formulate independently.** Record the engineering question, system boundary, quantities of interest, variables, units, candidate mechanisms, assumptions, and missing data before consulting AI.
2. **Ask within the permitted scope.** State what AI may and may not do; for example, “Critique these assumptions, but do not formulate or solve the final model.”
3. **Classify the output.** Distinguish definitions, conservation laws, constitutive or empirical relations, modelling assumptions, mathematical approximations, numerical approximations, factual claims, and interpretations.
4. **Make the decision.** Accept, modify, or reject each consequential suggestion for a technical reason.
5. **Verify independently.** Use mathematics, computation, trusted sources, or observations appropriate to the claim. A second answer from the same AI is not independent verification.
6. **Disclose material assistance.** Submit the declaration and process evidence required by Section 10.
7. **Defend the result.** Be prepared to reconstruct, modify, and explain the work without AI.

The operative logic is

$$
\text{AI proposal}
\rightarrow \text{critical test}
\rightarrow \text{independent evidence}
\rightarrow \text{student decision}.
$$

## 7. Permitted uses, when the assigned level allows them

Examples of legitimate uses include:

- explaining a concept after the student has attempted to understand it;
- criticizing an explicit set of assumptions or boundary conditions;
- proposing competing models $M_0,M_1,M_2$ with different complexity;
- suggesting dimensionless groups, limiting regimes, failure modes, or discriminating experiments;
- checking a student derivation, asymptotic expansion, sign convention, or dimensional calculation;
- helping to implement or debug an algorithm already connected to a stated mathematical model;
- proposing verification tests such as limiting cases, manufactured solutions, convergence studies, conservation checks, or comparisons with an independent method;
- generating literature-search terms or candidate references that the student then verifies in the original sources;
- editing language and presentation after the technical content has been established, when editorial assistance is permitted.

Permission to use AI does not imply that its output is correct, citable evidence, or suitable for submission without substantial student review.

## 8. Prohibited conduct

Unless a task explicitly authorizes it, students must not:

- use generative AI in an AI-0 activity;
- ask AI to produce a finished answer when the assigned level permits only explanation, criticism, suggestions, checking, or coding assistance;
- submit assumptions, equations, derivations, code, figures, references, data, or conclusions that they cannot reconstruct and defend;
- allow AI to make the final choice of system boundary, model, approximation regime, validation criterion, or engineering recommendation;
- present AI output as independent verification or as a scholarly source;
- invent, retain, or cite references, quotations, data, parameter values, experiments, or standards that have not been checked in the original source;
- conceal material AI use, falsify an AI-use declaration, or omit decision-relevant interactions when a log is required;
- use AI to paraphrase copied material in order to disguise plagiarism;
- upload confidential, proprietary, personal, assessment-restricted, export-controlled, or unpublished data or code without explicit authorization;
- use another student’s work as input to an AI system without permission;
- use AI to circumvent an assessment restriction or impersonate independent competence.

## 9. Verification obligations

The standard is not “the answer looks plausible” or “the code runs.” Students must match the evidence to the claim.

| Claim or output | Minimum expected checks |
|---|---|
| Equation or algebraic derivation | Independent reconstruction, substitution, and internal consistency |
| Physical model | Units, signs, conservation structure, constitutive assumptions, and trusted scientific sources |
| Boundary or initial condition | Mathematical compatibility and physical justification |
| Scaling or approximation | Dimensionless control parameter, limiting regime, error order where available, and possible nonuniform failure near boundaries, interfaces, or long times |
| Numerical result | Exact or manufactured solution where possible, refinement or convergence study, conservation/bounds, solver-tolerance study, or independent method |
| Parameter value or technical fact | Inspection of an appropriate primary source, standard, trusted database, or course text |
| Physical prediction | Numerical verification plus comparison with independent observational or experimental evidence where available |
| Engineering decision | Validated model evidence, sensitivity or uncertainty analysis, and an explicit statement of limitations |

Students must preserve the distinction

$$
\text{verification: did we solve the chosen model correctly?}
$$

from

$$
\text{validation: is the chosen model adequate for reality and purpose?}
$$

A numerically converged solution may be verified yet physically invalid.

## 10. Disclosure and process evidence

Disclosure is required whenever AI materially affects submitted reasoning, mathematics, code, figures, prose, references, or conclusions. Pure spelling or formatting assistance need not be logged unless it changes technical content. When uncertain, disclose.

For ordinary assignments, include this statement at the end of the submission:

```text
AI USE DECLARATION
Permitted level for this task:
Tool(s) used and date(s):
Purpose of use:
Material contributions retained in the submission:
How those contributions were independently checked:
Important suggestions modified or rejected, and why:
```

If no generative AI was used, write:

```text
AI USE DECLARATION
I did not use generative AI in preparing this submission.
```

For projects, students must retain decision-relevant process evidence, which may include:

- the timestamped AI-free initial formulation;
- an assumptions register and modelling decision log;
- concise records of prompts or interactions that materially changed the work;
- accepted, modified, and rejected AI suggestions;
- verification and validation evidence;
- version history for code, analysis, and reports.

A complete transcript of every minor interaction is not normally required. The record must be sufficient to show the provenance of consequential decisions. AI disclosure is not a substitute for citing the original scientific sources.

## 11. Sources and citations

AI should be treated as a query generator, not as a bibliographic database. The required chain is

$$
\text{AI suggestion}
\rightarrow \text{search}
\rightarrow \text{original source}
\rightarrow \text{inspection}
\rightarrow \text{verified claim}.
$$

In particular:

- verify that every title, author, publication venue, year, DOI, and URL exists;
- locate quotations in the original document;
- obtain material properties and numerical constants from appropriate data sources;
- use textbooks for established mathematical and physical models, primary literature for contemporary technical claims, and official documents for standards and procedures;
- cite the source actually inspected, not the AI system that suggested it.

## 12. Programming and computational work

Students must distinguish

$$
\text{physical model}
\neq \text{mathematical model}
\neq \text{algorithm}
\neq \text{implementation}
\neq \text{numerical result}.
$$

AI-assisted code is acceptable only at the permitted level and only when the student can:

1. state which equations and approximations the program implements;
2. explain the numerical method and its expected accuracy, stability, and limitations;
3. map important terms in the model to the corresponding parts of the code;
4. test the implementation using appropriate benchmarks, refinement, invariants, or independent calculations;
5. interpret failures and results without relying on AI-generated explanations.

“The code ran” means only that one execution terminated without a fatal software error. It does not establish mathematical correctness, numerical convergence, or physical validity.

## 13. Intellectual ownership and assessment

In this course, intellectual ownership does not require every intermediate sentence or line of code to have been produced without assistance. It requires that the student can **reconstruct, justify, test, modify, and defend every consequential modelling choice**.

Marks are awarded for modelling judgement, reasoning, evidence, verification, interpretation, and communication—not for the sophistication of the AI tool or prompt. The instructor may use an oral defence, changed parameters, a request for an alternative model, or reconstruction of a derivation or algorithm to assess understanding and ownership.

Using AI above the authorized level, using it during an AI-0 assessment, concealing material use, or submitting work that is not intellectually owned may constitute unauthorized assistance or academic misconduct under applicable university procedures. Automated AI-detection scores will not be treated as sufficient evidence on their own.

Permission to use AI does not change individual or group authorship rules. Students must still follow the stated collaboration policy and identify the contributions of human collaborators.

## 14. Privacy, confidentiality, copyright, and access

- Do not enter personal data, confidential industrial information, unpublished research, restricted assessment material, licensed content, or third-party code into an AI service unless its use is explicitly authorized.
- Respect copyright, licences, attribution requirements, and the terms governing datasets and software.
- Students will not be required to purchase a premium AI subscription to complete an assessed task. If a particular AI tool is required, an institutionally available or equivalent accessible route will be specified.
- Students who cannot use a permitted AI system for accessibility, privacy, technical, or ethical reasons should contact the instructor for an equivalent route without academic disadvantage.

## 15. Student responsibility statement

By submitting work, the student accepts responsibility for every assumption, equation, parameter, citation, line of code, numerical result, uncertainty statement, interpretation, and conclusion included in the submission, irrespective of whether AI assistance was permitted or used.

Before submitting, the student should be able to answer:

1. What did I formulate before using AI?
2. Which parts were influenced by AI?
3. Which AI suggestions did I accept, modify, or reject, and why?
4. What independent evidence supports each consequential claim?
5. Where can the model, approximation, computation, or conclusion fail?
6. Can I reproduce and defend the work without AI?

## 16. Policy changes

Task-specific permissions will be stated in writing. Material revisions to this policy will be announced and dated; they will not be applied retroactively to work already submitted.

---

> **Compact rule:** Think first. Use AI only at the authorized level. Treat its output as a hypothesis. Decide yourself. Verify independently. Disclose material assistance. Remain responsible.
