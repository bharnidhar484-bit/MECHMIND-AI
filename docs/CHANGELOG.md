# Changelog

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## [1.0.0] - 2026-04-13

### Added
- Initial Streamlit chatbot interface for MechMind AI
- Domain-restricted system prompt for mechanical engineering topics
- Session-based chat history using `st.session_state`
- Sidebar with project description, example questions, and `Clear Chat`
- User and assistant avatars in chat messages
- Footer disclaimer for AI-generated answers
- Gemini API smoke test script
- Documentation set under `docs/`

### Changed
- Default model routing aligned to an active Gemini Flash alias for deployment stability
- Error handling improved with user-friendly messages for auth, quota, and model failures

### Fixed
- Environment loading configured for both local `.env` use and hosted secret injection
- Deployment path validated for Hugging Face Spaces with `app.py` as the entry point

## Version 1.0.0 Notes

### Features Added
- Mechanical engineering chat assistant
- Streamlit-based frontend
- Gemini integration
- Sidebar guidance and session reset
- Deployment-ready environment handling

### Tech Decisions Made
- Streamlit chosen for rapid UI delivery
- `python-dotenv` used for local secret loading
- Gemini Flash-family model used for low-cost text generation
- Hugging Face Spaces selected as the default hosting target
