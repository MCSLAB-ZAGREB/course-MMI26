# Setting up and using ChatGPT for this course

## 1. Create your course project

1. Open ChatGPT.
2. Create a new **Project**.
3. Name it:

```text
Mathematical Modelling in Engineering — Your Name
```

Always start course-related chats inside this project. The project preserves the same instructions and course sources across its chats.

## 2. Add the Project Instructions

Open the project settings and locate the **Instructions** field.

Open:

```text
00_CHATGPT_PROJECT_INSTRUCTIONS.md
```

Copy its complete contents into the project’s **Instructions** field.

Do not use uploading the instructions file as a substitute for this step. The Instructions field controls how ChatGPT should behave in every project chat.

These instructions configure ChatGPT to act as a mathematical-modelling mentor: it should teach, ask relevant questions, provide progressive hints, criticize reasoning, and avoid silently completing modelling decisions for you.

## 3. Upload the course sources

Upload the following file to the project’s **Sources** section:

```text
00_Course_AI_Policy.md
```

This document defines the permitted AI levels, disclosure requirements, prohibited uses, and your responsibility for submitted work.

When provided by the instructor, also upload other files.


## 4. Start a separate chat for each substantial task

Do not use one enormous chat for the entire course. Start a new project chat for each distinct topic or outcome, for example:

```text
Regular perturbation practice
Boundary-layer problem
Cooling-model assignment
Fourier-method revision
Semester-project model review
```

This keeps the reasoning focused while retaining the shared project instructions and course sources.

## 5. Select the appropriate mode

Begin by telling ChatGPT what kind of help you need.

### Technique-learning mode

Use this when learning a mathematical method such as perturbation theory, boundary layers, multiple scales, nondimensionalization, Fourier methods, or fundamental solutions.

Example:

> Technique-learning mode. Explain the difference between regular and singular perturbations. Begin with the main idea, derive a simple example, and then give me one question to test my understanding.

In this mode, ChatGPT should teach the method directly. It should not force you through the complete modelling checklist unless the modelling context is relevant to the mathematics.

### Modelling mode

Use this when constructing, simplifying, validating, or interpreting an engineering model.

Begin with:

```text
Modelling mode
Problem:
What must be predicted or decided:
Graded or ungraded:
Permitted AI level:
My independent formulation:
Where I am stuck:
```

ChatGPT will guide you through the relevant modelling questions concerning system boundaries, variables, units, scales, assumptions, conservation laws, constitutive relations, boundary and initial conditions, dimensionless parameters, approximations, verification, validation, uncertainty, and interpretation.

It should ask only the next few relevant questions, not the entire checklist at once.

### Review mode

Use this when you already have a model, derivation, approximation, interpretation, or program.

Example:

> Review mode. Here is my nondimensionalization. Identify the first consequential error or unsupported choice. Explain why it matters, but let me correct it.

## 6. Show your attempt

Do not begin only with:

> Solve this problem.

Instead, show your current reasoning:

> I think this is a singular perturbation because setting \(\varepsilon=0\) reduces the order of the equation. I do not know how to determine the boundary-layer location. Give me the smallest useful hint.

You can control the amount of assistance:

* “Ask me questions before giving a hint.”
* “Give me only the next step.”
* “Explain the underlying principle.”
* “Show me an analogous example.”
* “Check my derivation but do not continue it.”
* “Give me a more direct explanation.”
* “Challenge my assumptions.”
* “Ask me to interpret the result.”

ChatGPT may sometimes respond with questions rather than an immediate answer. This is intentional. The purpose is to help you develop the reasoning required to formulate and assess models independently.

## 7. Use ChatGPT productively

Appropriate uses include:

* learning mathematical concepts and methods;
* checking units, signs, algebra, or asymptotic ordering;
* criticizing assumptions and conditions;
* comparing alternative models or solution methods;
* identifying limiting regimes and failure mechanisms;
* proposing verification tests;
* debugging code after stating the model and numerical algorithm;
* asking what evidence would validate or invalidate a model.

Inappropriate uses include:

* requesting a finished graded assignment;
* copying equations without understanding their origin;
* submitting generated derivations or code without verification;
* treating ChatGPT as a scientific source;
* assuming that plausible prose, a small residual, or working code establishes correctness.

## 8. Finish with an audit

Before considering the work complete, ask:

> Audit my work using the course modelling checklist. Do not repair it automatically. Identify what I still need to justify, verify, validate, quantify, or interpret.

You remain responsible for every assumption, equation, approximation, parameter, citation, numerical result, and conclusion you submit.

You own the work only if you can reconstruct it, modify it, test it, and defend every consequential choice without ChatGPT.

Always follow the AI level specified for the activity. Do not use ChatGPT during AI-0 assessments.
