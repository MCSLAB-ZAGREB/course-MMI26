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
- use vector analysis (gradient, divergence, the divergence theorem) to pass from integral to differential balance laws;
- derive continuum models from conservation laws and constitutive closures;
- nondimensionalize ODE/PDE models and interpret dimensionless groups such as the Péclet and Biot numbers;
- identify dominant balances and justify neglected terms quantitatively;
- distinguish regular and singular perturbations and construct boundary-layer approximations;
- model advection, diffusion, and advection–diffusion of mass, and heat transfer, and compare Fick's law, Fourier's law, and Newton's law of cooling;
- solve linear problems with Fourier series and separation of variables, self-similar and fundamental solutions, and superposition;
- recognize multiple spatial scales, derive homogenized (effective) models, and state their limitations;
- take a model from industrial practice through the whole pipeline, including calibration against data and uncertainty;
- verify analytical and numerical calculations independently;
- compare models, state validity and uncertainty, and defend conclusions.

## Semester scope

| Week | Canonical topic | Related textbook chapters (indicative) |
|---:|---|---|
| 1 | Introduction to mathematical modelling; dimensional analysis | 1, 4 |
| 2 | Continuum modelling; vector analysis | 2 |
| 3 | Conservation law; constitutive laws | 2 |
| 4 | Regular perturbations; nondimensionalization of models | 4, 6 |
| 5 | Singular perturbations; boundary layer | 6, 7 |
| 6 | Advection and mass transport | 2 |
| 7 | Mass diffusion; advection–diffusion models | 2; 7 for advection-dominated layers |
| 8 | Midterm examination: Weeks 1–7 | — |
| 9 | Heat transfer | 2; 1 for lumped (Newton cooling) models |
| 10 | Fourier series; method of separation of variables | No dedicated chapter; search the book |
| 11 | Self-similar and fundamental solutions | 5 |
| 12 | Multiple spatial scales; homogenization | 8, 11; search for homogenization |
| 13 | A model from industrial practice | 12 |
| 14 | A model from industrial practice | 12 |
| 15 | Final examination | — |

The chapter column is inferred from chapter titles, not from a section-by-section comparison with the lectures. Confirm each link by searching the textbook and do not force a match. Chapters 3, 9, and 10 have no corresponding week; 9 and 10 may still supply perturbation examples.

Topics build on each other in this order. Practice for the midterm stays within Weeks 1–7.

## Canonical distinctions and conventions

Keep distinct

$$
\text{reality}\neq\text{observations}\neq\text{model}
\neq\text{model solution}\neq\text{interpretation}\neq\text{decision}.
$$

Also distinguish data from assumptions, conservation laws from constitutive laws, regular from singular perturbations, formal expansions from justified approximations, microscale from effective (homogenized) descriptions, numerical error from model discrepancy, and verification from validation.

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

- cooling and heat conduction: scales, lumped/distributed models, boundary conditions, Fourier series and separation of variables;
- chemical or pollutant transport: conservation, advection and diffusion, diffusion length, kernels, and sources;
- advection-dominated transport: the Péclet number, regular versus singular limits, and boundary layers;
- layered, porous, composite, battery, drying, or manufacturing systems: effective (homogenized) properties, calibration, uncertainty, and validation.

Derive common engineering rules of thumb rather than assuming them, for example: lumped-capacitance cooling when the Biot number $\mathrm{Bi}=hL/k\ll1$; the diffusion length $\sqrt{Dt}$; advection versus diffusion from the Péclet number $\mathrm{Pe}=UL/D$; a boundary-layer thickness of order $L/\mathrm{Pe}$ in steady advection–diffusion; the effective conductivity of a layered composite (arithmetic mean along the layers, harmonic mean across them). State where each rule fails.

## Course boundaries

The assessed core is modelling judgement supported by analysis and transparent computation. This is not a comprehensive course in PDE theory, numerical analysis, programming, fluid mechanics, electromagnetics, optimization, or machine learning. Material beyond these boundaries, such as rigorous asymptotic theory or the convergence theory of homogenization, is optional enrichment and should be labelled as such.

Computation should test reasoning, not replace formulation. Before computing, establish the model, method, expected behaviour, and an independent check. A converged calculation may still solve an inadequate model.

For every result ask: What is represented or neglected? Which scales control the regime? Why are the model and method justified? How was the result checked? Where does it fail? What conclusion follows?
