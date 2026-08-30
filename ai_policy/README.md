# How to use ChatGPT in this course

ChatGPT is configured to act as a mathematical-modelling mentor, not as an automatic problem solver. Its purpose is to help you formulate better questions, identify assumptions, choose appropriate methods, detect errors, and evaluate whether a result can be trusted.

It may respond by asking you questions instead of immediately giving an answer. This is intentional: modelling decisions must remain yours.

## Begin by selecting the type of help

Tell ChatGPT which mode you need.

### 1. Technique-learning mode

Use this when learning a mathematical method such as perturbation theory, boundary layers, multiple scales, nondimensionalization, Fourier methods, or fundamental solutions.

Example:

> Technique-learning mode. Explain the difference between regular and singular perturbations. Start with the main idea, derive a simple example, and then give me one question to check my understanding.

In this mode, ChatGPT should teach the method directly. It will not ask about the complete engineering context unless that context matters mathematically.

### 2. Modelling mode

Use this when constructing or analysing a model of an engineering situation.

Begin with:

```text
Modelling mode
Problem:
What must be predicted or decided:
Permitted AI level:
My initial formulation:
Where I am stuck:
```

ChatGPT will guide you through relevant questions concerning the system boundary, variables, units, scales, assumptions, balance laws, constitutive relations, conditions, approximations, verification, validation, uncertainty, and interpretation.

It should ask only the next few relevant questions—not the entire checklist at once.

### 3. Review mode

Use this when you already have a model, derivation, approximation, or program.

Example:

> Review mode. Here is my nondimensionalization. Identify the first consequential error or unsupported choice. Explain why it matters, but let me correct it.

## Show your attempt

Do not begin with only:

> Solve this problem.

Instead, show what you understand and identify your difficulty:

> I think this is a singular perturbation because setting \(\varepsilon=0\) reduces the order of the equation. I do not know how to determine the boundary-layer location. Give me the smallest useful hint.

You may control the amount of assistance:

* “Ask me questions before giving a hint.”
* “Give me only the next step.”
* “Show me an analogous example.”
* “Check my derivation but do not continue it.”
* “Give a more direct explanation.”
* “Challenge my assumptions.”
* “Ask me to interpret the result physically.”

## Use ChatGPT productively

Good uses include:

* explaining a mathematical concept;
* checking units, signs, algebra, or asymptotic ordering;
* criticizing assumptions and boundary conditions;
* comparing alternative models or methods;
* identifying possible limiting regimes;
* suggesting verification tests;
* debugging code after you have specified the model and algorithm;
* asking what evidence would validate or invalidate a model.

Poor uses include:

* requesting a finished assignment;
* accepting equations without understanding their origin;
* copying generated derivations or code without checking them;
* treating ChatGPT as a scientific source;
* assuming that plausible prose or working code establishes correctness.

## Remain responsible

ChatGPT can be wrong, overconfident, or based on assumptions you did not intend. You remain responsible for every equation, approximation, parameter, citation, numerical result, and conclusion you submit.

Before finishing, ask:

> Audit my work using the course modelling checklist. Do not repair it automatically. Identify what I still need to justify, verify, validate, or interpret.

You understand and own the work only if you can reconstruct it, modify it, test it, and defend every consequential modelling choice without ChatGPT.

Always follow the AI level specified for the activity. Do not use ChatGPT during AI-0 assessments.
