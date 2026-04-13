---
title: MechMind AI
emoji: 🤖
colorFrom: blue
colorTo: gray
sdk: docker
app_port: 8501
pinned: false
---

# MechMind AI

<p align="center">
  <strong>Domain-focused AI assistant for mechanical engineering learning, revision, and problem solving.</strong>
</p>

<p align="center">
  <a href="https://github.com/bharnidhar484-bit/MECHMIND-AI">GitHub Repository</a>
  |
  <a href="https://huggingface.co/spaces/bharnidhar484/mechmind-ai">Hugging Face Space</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Streamlit-1.54.0-FF4B4B?style=flat-square&logo=streamlit" alt="Streamlit 1.54.0">
  <img src="https://img.shields.io/badge/Gemini-Flash_API-4285F4?style=flat-square&logo=google" alt="Gemini Flash API">
  <img src="https://img.shields.io/badge/Deployment-Hugging_Face_Spaces-FCC624?style=flat-square" alt="Hugging Face Spaces">
  <img src="https://img.shields.io/badge/Status-In_Development-orange?style=flat-square" alt="In Development">
</p>

## Overview

MechMind AI is a Streamlit-based chatbot built for mechanical engineering students and early-career engineers. It uses the Gemini API to answer questions across thermodynamics, fluid mechanics, machine design, manufacturing, materials, and AI applications in mechanical engineering. The application is intentionally scoped to this domain so that responses stay relevant, structured, and academically useful.

## Why This Project Exists

Mechanical engineering students often need fast help with concept revision, derivations, problem breakdowns, material selection logic, and engineering applications of AI. General-purpose chatbots can answer these questions, but they are not always focused. MechMind AI narrows the problem space to deliver a cleaner academic assistant that is easier to use, cheaper to deploy, and simpler to maintain.

## Core Capabilities

- Answers only within the defined mechanical engineering scope
- Maintains chat history during the active Streamlit session
- Provides a clean chat interface with sidebar guidance and example questions
- Shows user-friendly messages for API, model, quota, and connectivity issues
- Reads secrets from environment variables, which makes it ready for Hugging Face Spaces
- Includes a lightweight Gemini smoke test script for setup verification

## Supported Scope

| Area | Coverage |
|---|---|
| Thermodynamics | laws, cycles, entropy, efficiency, energy balances |
| Heat transfer | conduction, convection, radiation, heat exchangers |
| Fluid mechanics | Bernoulli, continuity, Reynolds number, flow behavior |
| Machine design | shafts, gears, bearings, springs, factor of safety |
| Mechanics of materials | stress, strain, bending, torsion, failure criteria |
| Manufacturing | casting, machining, welding, forming, additive methods |
| Materials science | selection, fatigue, corrosion, fracture, high-temperature behavior |
| AI in mechanical engineering | predictive maintenance, digital twins, smart manufacturing, generative design |

## What The App Looks Like

The current UI includes:

- a professional hero section
- chat messages with user and assistant avatars
- a sidebar with project description, example prompts, and `Clear Chat`
- a bottom disclaimer reminding users to verify critical calculations
- a loading spinner during Gemini requests

## Architecture Snapshot

```text
User
  |
  v
Streamlit UI (app.py)
  |
  v
Python app logic
  |
  v
Gemini API (Flash model)
  |
  v
Response rendering + session history
```

## Technology Stack

| Layer | Technology | Version |
|---|---|---|
| Language | Python | 3.11 runtime, 3.10+ compatible |
| UI | Streamlit | 1.54.0 |
| AI SDK | google-generativeai | 0.8.6 |
| Environment loading | python-dotenv | 1.2.1 |
| Deployment | Hugging Face Spaces | Docker SDK |

## Repository Structure

```text
MECHMIND-AI/
|-- app.py
|-- test_gemini.py
|-- requirements.txt
|-- Dockerfile
|-- .dockerignore
|-- .env.example
|-- .gitignore
|-- README.md
`-- docs/
    |-- PROJECT_OVERVIEW.md
    |-- SYSTEM_DESIGN.md
    |-- API_REFERENCE.md
    |-- USER_GUIDE.md
    |-- DEVELOPMENT_GUIDE.md
    |-- CHANGELOG.md
    `-- FUTURE_SCOPE.md
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/bharnidhar484-bit/MECHMIND-AI.git
cd MECHMIND-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a local `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-flash-latest
```

### 4. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### 5. Optional smoke test

```bash
python test_gemini.py
```

## Deployment To Hugging Face Spaces

This repository is prepared for Hugging Face Spaces using the Docker SDK.

### Required Space settings

- SDK: `Docker`
- App port: `8501`
- Secret: `GEMINI_API_KEY`

### Deployment flow

1. Create a new Space on Hugging Face.
2. Select `Docker` as the SDK.
3. Import or connect this GitHub repository.
4. Add `GEMINI_API_KEY` in Space Secrets.
5. Deploy the Space and verify the chat loads correctly.

The container starts Streamlit with:

```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

## Example Questions

```text
Explain Bernoulli's theorem with a practical example.
How do I calculate Reynolds number for pipe flow?
What is the difference between ductile and brittle fracture?
How is AI used in predictive maintenance for rotating machinery?
Recommend a material for a high-temperature turbine blade.
Solve a torsion problem for a solid circular shaft.
Compare casting and forging for part manufacturing.
What is the purpose of factor of safety in machine design?
Explain the second law of thermodynamics in simple terms.
What is a digital twin in manufacturing?
```

## Documentation

Detailed project documentation is available in the [`docs/`](./docs) folder:

- [`PROJECT_OVERVIEW.md`](./docs/PROJECT_OVERVIEW.md)
- [`SYSTEM_DESIGN.md`](./docs/SYSTEM_DESIGN.md)
- [`API_REFERENCE.md`](./docs/API_REFERENCE.md)
- [`USER_GUIDE.md`](./docs/USER_GUIDE.md)
- [`DEVELOPMENT_GUIDE.md`](./docs/DEVELOPMENT_GUIDE.md)
- [`CHANGELOG.md`](./docs/CHANGELOG.md)
- [`FUTURE_SCOPE.md`](./docs/FUTURE_SCOPE.md)

## Important Notes

- The current implementation defaults to `gemini-flash-latest`.
- Earlier drafts referenced `gemini-1.5-flash`, but that model is no longer the production default in this repository.
- The application is designed for learning support, not as a substitute for engineering judgment.
- Critical calculations should always be verified independently.

## Project Status

Current status: `In Development`

The core chat workflow, Gemini integration, documentation set, and Hugging Face deployment path are in place. Future work includes richer study features such as PDF support, equation rendering, and quiz generation.

## License

No license file has been added to this repository yet.
