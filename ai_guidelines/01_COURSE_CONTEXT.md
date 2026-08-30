# Mathematical Modelling in Engineering — Course Context

This file defines course-specific content and scope. ChatGPT behaviour, student responsibility, and assessment rules are governed separately.

## Course identity

The course teaches students to construct, simplify, solve, test, interpret, and defend engineering models. It connects applied mathematics, engineering physics, numerical modelling, and scientific computing.

The subject is not memorizing equations but deciding which model is justified by purpose, mechanisms, scales, assumptions, evidence, and the required decision.

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
- verify analytical and numerical calculations independently;
- compare models, state validity and uncertainty, and defend conclusions.

## Semester scope

| Week | Canonical topic |
|---:|---|
| 1 | Dimensional analysis and characteristic quantities |
| 2 | Nondimensionalization and scaling |
| 3 | Dominant balance and regular perturbations |
| 4 | Singular perturbations |
| 5 | Emergence of a boundary layer |
| 6 | Multiple time scales |
| 7 | Continuum modelling: conservation and constitutive laws |
| 8 | Midterm examination: Weeks 1–7 |
| 9 | Fick’s law, Fourier’s law, and Newton’s law of cooling |
| 10 | Fourier method |
| 11 | Fundamental solutions and superposition |
| 12 | Multiscale problems |
| 13 | Industrial modelling I: problem formulation |
| 14 | Industrial modelling II: calibration, uncertainty, validation, decisions |
| 15 | Final examination: integrated modelling workflow |

## Canonical distinctions and conventions

Keep distinct

$$
\text{reality}\neq\text{observations}\neq\text{model}
\neq\text{model solution}\neq\text{interpretation}\neq\text{decision}.
$$

Also distinguish data from assumptions, conservation laws from constitutive laws, numerical error from model discrepancy, and verification from validation.

Unless an activity states otherwise:

- use SI units and define every symbol, domain, parameter, source, and condition;
- use $x$ for position, $t$ for time, and explicitly defined characteristic scales;
- write dimensionless variables as $x^*=x/L$, $t^*=t/T_c$, or define an alternative;
- use $0<\varepsilon\ll1$ for a small dimensionless parameter;
- use $\mathbf n$ for the outward normal and state all flux/source signs;
- justify omissions by dimensionless size, asymptotic order, data, or an explicit argument.

The canonical conservation and gradient-flux forms are

$$
\frac{\partial u}{\partial t}+\nabla\cdot\mathbf J=s,
\qquad
\mathbf J_c=-D\nabla c,
\qquad
\mathbf q=-k\nabla T,
$$

with $D,k>0$. For outward heat loss,

$$
-k\frac{\partial T}{\partial n}=h(T-T_\infty),\qquad h\ge0.
$$

## Recurring engineering contexts

Prefer examples that connect several topics:

- cooling and heat conduction: scales, lumped/distributed models, boundary conditions, Fourier modes;
- chemical or pollutant diffusion: conservation, diffusion length, kernels, and sources;
- weakly perturbed oscillators and advection–diffusion: secular behaviour, multiple scales, and boundary layers;
- layered, porous, composite, battery, drying, or manufacturing systems: effective behaviour, calibration, uncertainty, and validation.

## Course boundaries

The assessed core is modelling judgement supported by analysis and transparent computation. This is not a comprehensive course in PDE theory, numerical analysis, programming, fluid mechanics, electromagnetics, optimization, or machine learning.

Computation should test reasoning, not replace formulation. Before computing, establish the model, method, expected behaviour, and an independent check. A converged calculation may still solve an inadequate model.

For every result ask: What is represented or neglected? Which scales control the regime? Why are the model and method justified? How was the result checked? Where does it fail? What conclusion follows?
