# System Design

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## System Architecture
```text
┌───────────────┐
│     User      │
└───────┬───────┘
        │ question
        v
┌───────────────┐
│ Streamlit UI  │
│ app.py        │
└───────┬───────┘
        │ session state + prompt assembly
        v
┌───────────────┐
│ Python Logic  │
│ env + guards  │
└───────┬───────┘
        │ API request
        v
┌───────────────┐
│ Gemini API    │
│ Flash model   │
└───────┬───────┘
        │ response text
        v
┌───────────────┐
│ Streamlit UI  │
│ chat output   │
└───────────────┘
```

## Component Breakdown

### Frontend
- Built with Streamlit chat primitives
- Displays the application header, subtitle, sidebar, chat history, and disclaimer
- Uses avatars to visually distinguish user and assistant messages

### Backend
- Implemented in `app.py`
- Loads environment variables using `python-dotenv`
- Builds the full conversation transcript before sending the next request
- Maintains in-memory session state for active chat continuity

### AI Layer
- Uses the Google Gemini API through `google-generativeai`
- Applies a system instruction that restricts output to mechanical engineering topics
- Returns user-friendly messages when the upstream model is unavailable or rate-limited

### Deployment
- Designed for Hugging Face Spaces with Streamlit
- Uses environment variables such as `GEMINI_API_KEY`
- Requires no custom server process or manual port configuration

## Data Flow
User Input -> Streamlit -> Python -> Gemini API -> Response

## Prompt Engineering Strategy
- A fixed system prompt defines the assistant role, allowed subjects, and decline behavior for out-of-scope questions.
- The latest user message is sent together with recent chat history to preserve conversational continuity.
- The instruction emphasizes accuracy, clarity, and student-friendly explanations.
- The model is guided to produce step-by-step reasoning when formulas or structured explanations are useful.

## Session State Management
- Chat history is stored in `st.session_state.messages`.
- Each message is stored with a `role` and `content`.
- A default assistant welcome message is created for new sessions.
- The sidebar `Clear Chat` button resets the session back to the default state.
- Session state is scoped to the active Streamlit session and does not persist across browser restarts.

## Error Handling Strategy
- Missing API keys trigger a visible warning in the UI.
- Model failures are mapped to user-friendly responses for common cases:
  - invalid API key
  - rate limit or quota exhaustion
  - unavailable or deprecated model name
  - generic connectivity or service issues
- A loading spinner is shown while the Gemini request is in progress.
