# API Reference

Version: v1.0  
Date: 2026-04-13  
Author: MechMind AI Team

## Overview
MechMind AI uses the Google Gemini Developer API for text generation. The current application code defaults to `gemini-flash-latest` through an environment variable override, which keeps the project aligned with active Flash-family models.

## Gemini API Setup
1. Create a Google AI Studio account.
2. Generate a Gemini API key.
3. Add the key to a local `.env` file or to your deployment secret store.
4. Ensure the application reads `GEMINI_API_KEY` from the environment.

## Model Configuration
- Current implementation default: `gemini-flash-latest`
- Optional override: `GEMINI_MODEL`
- Legacy project reference: `gemini-1.5-flash`

### Legacy Note
Earlier project planning referenced `gemini-1.5-flash`. Google shut down `gemini-1.5-flash` on September 29, 2025, so the production-ready code uses a current Flash alias instead.

## Request Structure
```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "What is Bernoulli's theorem?"
        }
      ]
    }
  ]
}
```

## Response Structure
```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Bernoulli's theorem states that..."
          }
        ]
      }
    }
  ]
}
```

## Python Usage Example
```python
import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-flash-latest")
response = model.generate_content("What is Bernoulli's theorem?")
print(response.text)
```

## Environment Variable Setup
```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-flash-latest
```

## Rate Limits
The free tier is model-specific and can change over time. Earlier drafts referenced `1500 req/day`, but current official Gemini quotas are lower and vary by model. Example free-tier figures from Google's published quota table include:

| Model | Free-tier RPD |
|---|---|
| Gemini 2.5 Flash | 250 |
| Gemini 2.5 Flash-Lite | 1000 |
| Gemini 2.0 Flash | 200 |
| Gemini 1.5 Flash (deprecated) | 50 |

Always check the live quota page before publishing hard limits in user-facing documentation.

## Error Codes And Handling
| Condition | Typical Signal | Meaning | Handling Strategy |
|---|---|---|---|
| Invalid key | 401 or 403 | API key rejected | Prompt user to update `GEMINI_API_KEY` |
| Model unavailable | 404 | Deprecated or invalid model name | Switch to a current Flash model alias |
| Rate limit | 429 | Free-tier quota or request burst exceeded | Retry later and show a friendly message |
| Server issue | 500 or 503 | Temporary upstream failure | Retry with backoff |
| Network failure | Connection timeout | Local or remote network issue | Ask user to retry after checking connectivity |

## cURL Example
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H "Content-Type: application/json" \
  -H "X-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "What is Bernoulli'\''s theorem?"
          }
        ]
      }
    ]
  }'
```
