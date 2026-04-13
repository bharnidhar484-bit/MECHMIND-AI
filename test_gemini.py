import os
import sys

import google.generativeai as genai
from dotenv import load_dotenv


QUESTION = "What is Bernoulli's theorem?"


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

    if not api_key:
        print("GEMINI_API_KEY is not set in .env or the environment.")
        return 1

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    try:
        response = model.generate_content(QUESTION)
    except Exception as error:
        print(f"Gemini request failed: {error}")
        return 1

    text = getattr(response, "text", "").strip()
    if not text:
        print("Gemini returned an empty response.")
        return 1

    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
