import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(
    page_title="MechMind AI",
    page_icon="🤖",
    layout="centered",
)

SYSTEM_PROMPT = """
You are MechMind AI, an academic assistant for mechanical engineering students.
You may only answer questions related to mechanical engineering, including:
- thermodynamics and heat transfer
- fluid mechanics and fluid machinery
- machine design, mechanics of materials, and engineering mechanics
- manufacturing processes, CAD/CAM, and production systems
- materials science, material selection, and failure analysis
- AI in mechanical engineering, including predictive maintenance, digital twins, smart manufacturing, and generative design

If a user asks about anything outside these areas, politely decline and ask them to keep the conversation focused on mechanical engineering.
Keep answers accurate, clear, and practical for students. When useful, explain step by step and include equations in plain text.
""".strip()

SUBTITLE = (
    "Focused help for thermodynamics, fluid mechanics, machine design, "
    "manufacturing, materials, and AI in mechanical engineering."
)
USER_AVATAR = "🧑‍🎓"
ASSISTANT_AVATAR = "🤖"
MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
WELCOME_MESSAGE = (
    "Ask a mechanical engineering question and I will keep the discussion "
    "within that domain."
)
EXAMPLE_QUESTIONS = [
    "Explain the second law of thermodynamics in simple terms.",
    "How do I calculate Reynolds number for pipe flow?",
    "What material is suitable for a high-temperature turbine blade?",
    "Solve a shaft design problem for torsional shear stress.",
    "How is AI used for predictive maintenance in rotating machinery?",
]


@st.cache_resource(show_spinner=False)
def get_model(api_key: str) -> genai.GenerativeModel:
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.4,
            "top_p": 0.9,
            "max_output_tokens": 1024,
        },
    )


def build_conversation_prompt(messages: list[dict[str, str]]) -> str:
    transcript = []
    for message in messages:
        speaker = "User" if message["role"] == "user" else "Assistant"
        transcript.append(f"{speaker}: {message['content']}")

    history = "\n\n".join(transcript)
    return (
        "Continue the conversation below and answer the latest user message.\n\n"
        f"{history}\n\nAssistant:"
    )


def extract_response_text(response) -> str:
    text = getattr(response, "text", "")
    if text:
        return text.strip()

    candidates = getattr(response, "candidates", None) or []
    if candidates:
        parts = getattr(candidates[0].content, "parts", [])
        combined_text = "".join(getattr(part, "text", "") for part in parts).strip()
        if combined_text:
            return combined_text

    return "I could not generate a response just now. Please try again."


def generate_reply(api_key: str, messages: list[dict[str, str]]) -> str:
    model = get_model(api_key)
    prompt = build_conversation_prompt(messages)
    response = model.generate_content(prompt)
    return extract_response_text(response)


def friendly_api_error(error: Exception) -> str:
    message = str(error).lower()

    if "429" in message or "quota" in message or "rate limit" in message:
        return (
            "Gemini is rate-limiting this request right now. Please wait a moment "
            "and try again."
        )

    if "401" in message or "403" in message or "api key" in message:
        return (
            "The Gemini API key was rejected. Update `GEMINI_API_KEY` and try again."
        )

    if "404" in message or "not found" in message or "model" in message:
        return (
            "The configured Gemini model is not available for this API key. "
            "Try a current Flash model such as `gemini-flash-latest`."
        )

    return (
        "I couldn't get a response from Gemini right now. Please check your API key, "
        "usage quota, or network connection and try again."
    )


def initialize_chat() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": WELCOME_MESSAGE}
        ]


def reset_chat() -> None:
    st.session_state.messages = [
        {"role": "assistant", "content": WELCOME_MESSAGE}
    ]


def render_message(role: str, content: str) -> None:
    avatar = USER_AVATAR if role == "user" else ASSISTANT_AVATAR
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)


def apply_styles() -> None:
    st.markdown(
        """
        <style>
            .main .block-container {
                max-width: 900px;
                padding-top: 2rem;
                padding-bottom: 1rem;
            }
            .hero {
                padding: 1.5rem 1.6rem;
                border: 1px solid #d7e0ea;
                border-radius: 20px;
                background: linear-gradient(135deg, #f6f9fc 0%, #ecf3fb 100%);
                margin-bottom: 1rem;
            }
            .hero h1 {
                margin: 0;
                color: #132238;
                font-size: 2.1rem;
            }
            .hero p {
                margin: 0.45rem 0 0;
                color: #425466;
                font-size: 1rem;
                line-height: 1.6;
            }
            [data-testid="stSidebar"] {
                border-right: 1px solid #e4ebf3;
            }
            [data-testid="stChatMessage"] {
                border: 1px solid #e4ebf3;
                border-radius: 18px;
                padding: 0.3rem;
            }
            .disclaimer {
                color: #5f6c7b;
                font-size: 0.85rem;
                margin-top: 0.35rem;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.header("About")
        st.write(
            "MechMind AI is a focused study assistant for mechanical engineering "
            "topics, from core subjects to AI applications in the field."
        )

        st.header("Example Questions")
        for question in EXAMPLE_QUESTIONS:
            st.write(f"- {question}")

        st.divider()
        if st.button("Clear Chat", use_container_width=True):
            reset_chat()
            st.rerun()


def main() -> None:
    # Hugging Face Spaces exposes secrets through environment variables.
    api_key = os.environ.get("GEMINI_API_KEY")
    initialize_chat()
    apply_styles()
    render_sidebar()

    st.markdown(
        f"""
        <div class="hero">
            <h1>MechMind AI 🤖</h1>
            <p>{SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not api_key:
        st.warning(
            "Set `GEMINI_API_KEY` in your environment or `.env` file to enable chat."
        )

    for message in st.session_state.messages:
        render_message(message["role"], message["content"])

    prompt = st.chat_input(
        "Ask a mechanical engineering question...",
        disabled=not api_key,
    )

    st.markdown(
        '<div class="disclaimer">AI-generated answers — verify critical calculations</div>',
        unsafe_allow_html=True,
    )

    if not prompt:
        return

    user_message = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_message)
    render_message(user_message["role"], user_message["content"])

    with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
        with st.spinner("Thinking through the engineering problem..."):
            try:
                reply = generate_reply(api_key, st.session_state.messages)
            except Exception as error:
                reply = friendly_api_error(error)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
