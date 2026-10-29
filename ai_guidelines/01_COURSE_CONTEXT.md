# Mathematical Modelling in Engineering — Course Context

This file defines course-specific content, scope, and conventions. ChatGPT behaviour, student responsibility, and assessment rules are governed separately.

## Course identity

The course teaches students to construct, simplify, solve, test, interpret, and defend engineering models. It connects applied mathematics, engineering physics, numerical modelling, and scientific computing.

The subject is not memorizing equations but deciding which model is justified by purpose, mechanisms, scales, assumptions, evidence, and the required decision.

The course is taught at graduate level to engineering students. Many are strong in computation but less experienced with asymptotics and modelling arguments; some bring research or industrial problems of their own.

## Course materials

All of the following are Project files.

- **This file:** canonical pipeline, capabilities, weekly scope, conventions, and boundaries.
- **Lecture PDFs:** detailed content, terminology, worked examples, and expected level for each week. The lectures, not the textbook, define what each week covers.
- **Textbook:** T. Witelski and M. Bowen, *Methods of Mathematical Modelling: Continuous Systems and Differential Equations*, Springer Undergraduate Mathematics Series, Springer, 2015. It deepens the lectures with derivations, alternative approaches, worked examples, and exercises. Its twelve chapters:
  - Part I, Formulation of Models: 1 Rate Equations; 2 Transport Equations; 3 Variational Principles; 4 Dimensional Scaling Analysis.
  - Part II, Solution Techniques: 5 Self-Similar Scaling Solutions of Differential Equations; 6 Perturbation Methods; 7 Boundary Layer Theory; 8 Long-Wave Asymptotics for PDE Problems; 9 Weakly-Nonlinear Oscillators; 10 Fast/slow Dynamical Systems; 11 Reduced Models for PDE Problems.
  - Part III, Case Studies: 12 Modelling in Applied Fluid Dynamics.

Order of authority for content and conventions: the activity at hand, then this file, then the lectures, then the textbook. The textbook never overrides course conventions; map its notation onto them.

Printed page numbers and PDF page numbers of the textbook differ. Cite the printed page where it is visible and label PDF page numbers as such.

## Canonical modelling pipeline

$$
\text{situation}\to\text{purpose and boundary}\to\text{variables, units, scales}
\to\text{mechanisms and assumptions}\to\text{balances and closures}
\to\text{equations and conditions}\to\text{nondimensionalization}
\to\text{regime and approximation}\to\text{solution}
\to\text{verification}\to\text{interpretation}\to\text{validation and decision}.
$$

The process is iterative: failed checks or new evidence may require revising earlier modelling choices.

## Expected capabilities

Students should learn to:

- identify variables, parameters, units, data, and characteristic scales;
- nondimensionalize ODE/PDE models and interpret dimensionless groups;
- identify dominant balances and justify neglected terms quantitatively;
- distinguish regular and singular perturbations, boundary layers, and multiple scales;
- derive continuum models from conservation laws and constitutive closures;
- derive and compare Fick diffusion, Fourier heat conduction, and Newton cooling;
- use Fourier methods, fundamental solutions, and superposition;
- recognize multiscale structure and limitations of effective models;
- calibrate parameters against data and carry uncertainty through to conclusions;
- verify analytical and numerical calculations independently;
- compare models, state validity and uncertainty, and defend conclusions.

## Semester scope

| Week | Canonical topic | Related textbook chapters (indicative) |
|---:|---|---|
| 1 | Dimensional analysis and characteristic quantities | 4 |
| 2 | Nondimensionalization and scaling | 4; 5 for similarity scalings |
| 3 | Dominant balance and regular perturbations | 6 |
| 4 | Singular perturbations | 6, 7 |
| 5 | Emergence of a boundary layer | 7 |
| 6 | Multiple time scales | 9, 10 |
| 7 | Continuum modelling: conservation and constitutive laws | 2; 1 for lumped rate models |
| 8 | Midterm examination: Weeks 1–7 | — |
| 9 | Fick’s law, Fourier’s law, and Newton’s law of cooling | 1, 2 |
| 10 | Fourier method | No dedicated chapter; search the book |
| 11 | Fundamental solutions and superposition | 5 |
| 12 | Multiscale problems | 8, 11 |
| 13 | Industrial modelling I: problem formulation | 12 |
| 14 | Industrial modelling II: calibration, uncertainty, validation, decisions | Lectures |
| 15 | Final examination: integrated modelling workflow | — |

The chapter column is inferred from chapter titles, not from a section-by-section comparison with the lectures. Confirm each link by searching the textbook and do not force a match. Chapter 3 has no corresponding week.

Topics build on each other in this order. Practice for the midterm stays within Weeks 1–7; the final integrates the whole workflow.

## Canonical distinctions and conventions

Keep distinct

$$
\text{reality}\neq\text{observations}\neq\text{model}
\neq\text{model solution}\neq\text{interpretation}\neq\text{decision}.
$$

Also distinguish data from assumptions, conservation laws from constitutive laws, regular from singular perturbations, formal expansions from justified approximations, numerical error from model discrepancy, and verification from validation.

Unless an activity states otherwise:

- use SI units and define every symbol, domain, parameter, source, and condition;
- use $x$ for position, $t$ for time, and explicitly defined characteristic scales;
- write dimensionless variables as $x^*=x/L$, $t^*=t/T_c$, or define an alternative;
- use $0<\varepsilon\ll1$ for a small dimensionless parameter;
- use $\mathbf n$ for the outward normal and state all flux/source signs;
- justify omissions by dimensionless size, asymptotic order, data, or an explicit argument;
- when another source, including the textbook, uses different notation or scalings, state the mapping to these conventions.

## Recurring engineering contexts

Prefer examples that connect several topics:

- cooling and heat conduction: scales, lumped/distributed models, boundary conditions, Fourier modes;
- chemical or pollutant diffusion: conservation, diffusion length, kernels, and sources;
- weakly perturbed oscillators and advection–diffusion: secular behaviour, multiple scales, and boundary layers;
- layered, porous, composite, battery, drying, or manufacturing systems: effective behaviour, calibration, uncertainty, and validation.

Derive common engineering rules of thumb rather than assuming them, for example: lumped-capacitance cooling when the Biot number $\mathrm{Bi}=hL/k\ll1$; the diffusion length $\sqrt{Dt}$; boundary-layer thickness from a dominant balance. State where each rule fails.

## Course boundaries

The assessed core is modelling judgement supported by analysis and transparent computation. This is not a comprehensive course in PDE theory, numerical analysis, programming, fluid mechanics, electromagnetics, optimization, or machine learning. Material beyond these boundaries, such as rigorous asymptotic theory or homogenization, is optional enrichment and should be labelled as such.

Computation should test reasoning, not replace formulation. Before computing, establish the model, method, expected behaviour, and an independent check. A converged calculation may still solve an inadequate model.

For every result ask: What is represented or neglected? Which scales control the regime? Why are the model and method justified? How was the result checked? Where does it fail? What conclusion follows?
