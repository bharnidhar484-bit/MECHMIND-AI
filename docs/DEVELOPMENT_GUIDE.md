# Development Guide

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## Prerequisites
- Python 3.10 or newer
- `pip`
- `git`
- A Gemini API key from Google AI Studio

## Local Setup
1. Clone the repository.
2. Enter the project folder.
3. Install dependencies.
4. Create a `.env` file with your Gemini API key.
5. Run the Streamlit app.

```bash
git clone https://github.com/bharnidhar484-bit/MECHMIND-AI.git
cd MECHMIND-AI
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-flash-latest
```

## Folder Structure
```text
MECHMIND-AI/
├── app.py
├── test_gemini.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── docs/
    ├── PROJECT_OVERVIEW.md
    ├── SYSTEM_DESIGN.md
    ├── API_REFERENCE.md
    ├── USER_GUIDE.md
    ├── DEVELOPMENT_GUIDE.md
    ├── CHANGELOG.md
    └── FUTURE_SCOPE.md
```

## Getting A Gemini API Key
1. Visit Google AI Studio.
2. Sign in with a Google account.
3. Create or select a project.
4. Generate a Gemini API key.
5. Store it in `.env` for local use or in deployment secrets for hosted environments.

## Running Locally
Run the Streamlit interface:

```bash
streamlit run app.py
```

Optional smoke test:

```bash
python test_gemini.py
```

## Deploying To Hugging Face Spaces
1. Create a new Hugging Face Space with the Streamlit SDK.
2. Push this repository to GitHub.
3. Connect the Space to the GitHub repository or upload the repo contents directly.
4. Add `GEMINI_API_KEY` to Space Secrets.
5. Redeploy the Space and verify the app loads successfully.

## Common Errors And Fixes
| Problem | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `GEMINI_API_KEY` missing | `.env` missing or secret not configured | Add the key to `.env` or Hugging Face Secrets |
| 404 model error | Deprecated model name | Use `gemini-flash-latest` or another current Flash model |
| 429 error | Free-tier quota exceeded | Retry later or move to a paid tier |
| Empty app on startup | Streamlit command not used | Start with `streamlit run app.py` |
