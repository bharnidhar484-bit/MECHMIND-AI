# User Guide

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## Accessing The App
After deployment, open the Hugging Face Space in a browser:

`https://huggingface.co/spaces/YOUR_USERNAME/mechmind-ai`

Replace `YOUR_USERNAME` with the final Hugging Face account name before publishing.

## How To Ask Questions
Enter a mechanical engineering question in the chat box and press Enter. The assistant responds best when the question includes enough technical context, assumptions, units, and the exact problem you want solved.

## Example Questions
1. What is the second law of thermodynamics?
2. Explain Bernoulli's theorem with a simple example.
3. How do I calculate Reynolds number for pipe flow?
4. Solve a torsion problem for a solid circular shaft.
5. What material is suitable for a marine shaft under cyclic loading?
6. Explain the difference between ductile and brittle fracture.
7. What is the purpose of a flywheel in mechanical systems?
8. Compare casting and forging for part manufacturing.
9. How is AI used in predictive maintenance for rotating equipment?
10. What is the significance of factor of safety in machine design?

## Supported Topics
| Topic Area | Example Coverage |
|---|---|
| Thermodynamics | laws of thermodynamics, cycles, entropy, efficiency |
| Heat transfer | conduction, convection, radiation, heat exchangers |
| Fluid mechanics | Bernoulli, continuity, Reynolds number, losses |
| Machine design | shafts, gears, bearings, springs, factor of safety |
| Mechanics of materials | stress, strain, bending, torsion, failure criteria |
| Manufacturing | casting, machining, welding, additive manufacturing |
| Materials science | selection, microstructure, corrosion, fatigue |
| AI in mechanical engineering | predictive maintenance, digital twins, smart manufacturing |

## Out Of Scope Topics
The assistant is intentionally restricted from answering outside the project domain. Examples include:

- general politics
- entertainment
- personal finance
- unrelated software debugging
- medical or legal advice
- non-mechanical school subjects

## Tips For Better Answers
- Include known values, units, and assumptions.
- Ask one technical question at a time when solving numericals.
- Specify whether you want a short explanation, derivation, or step-by-step solution.
- Mention if the response should be exam-focused, practical, or beginner-friendly.
- For design questions, describe loads, materials, environment, and constraints.

## FAQ

### 1. Why did the assistant refuse my question?
The application is limited to mechanical engineering and closely related AI topics. Questions outside that scope are declined by design.

### 2. Can it solve numerical problems?
Yes. It can explain equations, substitute values, and show step-by-step reasoning. Critical calculations should still be verified independently.

### 3. Does it remember previous messages?
Yes, within the current browser session. Chat history is stored in Streamlit session state until the session ends or the user clears the chat.

### 4. Can I use it without an API key?
End users on a deployed Hugging Face Space do not need to enter a key directly if the maintainer has already configured the secret. Local development does require `GEMINI_API_KEY`.

### 5. What should I do if the app shows an API error?
Retry after a short delay. Free-tier quota, service availability, or an invalid secret can all cause temporary failures.
