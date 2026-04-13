# Project Overview

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## Project Title
MechMind AI

## Tagline
An AI study assistant for mechanical engineering students.

## Description
MechMind AI is a domain-focused Streamlit chatbot built to support mechanical engineering learning and problem solving. The application combines a lightweight Python backend, a clean chat interface, and Google Gemini to answer questions across thermodynamics, fluid mechanics, machine design, manufacturing, materials, and AI applications in mechanical engineering. The product is designed for fast deployment, low operating cost, and simple maintenance.

## Goals And Objectives
1. Provide quick, structured explanations for core mechanical engineering topics.
2. Offer step-by-step support for conceptual and numerical problem solving.
3. Restrict responses to a clearly defined academic domain to reduce irrelevant output.
4. Deliver a simple web interface that students can use without installation.
5. Support low-cost deployment through Streamlit and Hugging Face Spaces.

## Target Audience
- Mechanical engineering students
- Engineering learners preparing for exams and interviews
- Early-career engineers who need quick concept refreshers
- Users exploring AI applications in mechanical engineering

## Key Features
| Feature | Description |
|---|---|
| Domain-specific assistant | Restricts responses to mechanical engineering and closely related AI topics |
| Streamlit chat interface | Web-based UI with chat history and sidebar guidance |
| Session memory | Stores conversation history in `st.session_state` during the active session |
| Example prompts | Sidebar includes ready-to-use question examples |
| Safe failure handling | Shows user-friendly messages for API, quota, and connectivity issues |
| Hugging Face ready | Reads secrets from environment variables and uses `app.py` as the entry point |

## Tech Stack
| Layer | Technology | Version | Cost |
|---|---|---|---|
| Language | Python | 3.10+ | Free |
| UI | Streamlit | 1.54.0 | Free |
| AI SDK | google-generativeai | 0.8.6 | Free tier available |
| Env management | python-dotenv | 1.2.1 | Free |
| Model routing | Gemini API | Flash family | Free tier available |
| Deployment | Hugging Face Spaces | Managed Streamlit runtime | Free tier available |

## Project Status
In Development
