---
title: MechMind AI
emoji: 🤖
colorFrom: blue
colorTo: gray
sdk: docker
app_port: 8501
pinned: false
---

# 🤖 MechMind AI — Intelligent Mechanical Engineering Assistant

<div align="center">

<!-- Reminder: replace YOUR_USERNAME and badge/demo links before publishing to Hugging Face Spaces. -->
[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-xl.svg)](https://huggingface.co/spaces/YOUR_USERNAME/mechmind-ai)

**An AI-powered chatbot that bridges Mechanical Engineering and Artificial Intelligence**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?style=flat-square&logo=streamlit)
![Gemini](https://img.shields.io/badge/Gemini_API-Free-green?style=flat-square&logo=google)
![Hosted](https://img.shields.io/badge/Hosted_on-HuggingFace-yellow?style=flat-square)
![Cost](https://img.shields.io/badge/Cost-₹0_Free-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

</div>

---

## 🚀 Live Demo

> **Click the button above** or go to:  
> 👉 `https://huggingface.co/spaces/YOUR_USERNAME/mechmind-ai`

No installation. No signup. Just open and ask your question.

---

## 📌 About the Project

**MechMind AI** is a domain-specific AI chatbot built for mechanical engineering students and professionals. It uses Google's **Gemini API** (free tier) as the AI brain and **Streamlit** as the web interface, deployed live on **Hugging Face Spaces** — completely free.

The chatbot can:
- Explain any mechanical engineering concept in simple terms
- Solve numerical problems step-by-step with formulas
- Recommend materials based on engineering conditions
- Answer questions about **AI in Mechanical Engineering** (predictive maintenance, generative design, digital twins)
- Help with exam preparation (thermodynamics, fluid mechanics, machine design, and more)

---

## 🧠 Topics Covered

| Mechanical Engineering | AI in Mech Engineering |
|---|---|
| Thermodynamics & Heat Transfer | Predictive Maintenance (ML) |
| Fluid Mechanics | Generative Design (AI-CAD) |
| Machine Design & Analysis | Digital Twins |
| Manufacturing Processes | Smart Manufacturing / Industry 4.0 |
| Material Science & Selection | Robotic Process Automation |
| Engineering Mechanics | Computer Vision in Quality Control |

---

## 📥 Input / Output

| Input (What you ask) | Output (What MechMind returns) |
|---|---|
| "Explain Bernoulli's theorem" | Concept explanation + derivation + real-world use |
| "Gear ratio: input 1200rpm, output 300rpm" | Step-by-step solution: GR = 4:1 |
| "Best material for high-temperature turbine blades?" | Recommends Inconel / Ti alloys with reasoning |
| "How does ML help in predictive maintenance?" | Explains sensor data + ML model workflow |
| "What is Von Mises stress criterion?" | Formula + physical meaning + failure condition |
| "Explain Carnot efficiency for Th=500K, Tc=300K" | Formula + substitution + η = 40% |

---

## 🛠️ Tech Stack

| Layer | Technology | Cost |
|---|---|---|
| Frontend / UI | Streamlit | Free |
| AI / LLM | Google Gemini 1.5 Flash API | Free (1500 req/day) |
| Backend | Python 3.10+ | Free |
| Version Control | GitHub | Free |
| Hosting | Hugging Face Spaces | Free forever |
| Secret Management | HF Spaces Secrets | Free |

**Total Cost: ₹0**

---

## 📁 Project Structure

```
mechmind-ai/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .gitignore              # Ignore .env and __pycache__
```

---

## ⚙️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/mechmind-ai.git
cd mechmind-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key
Get your free key at 👉 https://aistudio.google.com

Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## ☁️ Deploy to Hugging Face Spaces (Free)

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **New Space** → Choose **Streamlit** as SDK
3. Link this GitHub repository
4. Go to **Settings → Secrets** → Add `GEMINI_API_KEY`
5. Space auto-deploys and gives you a public URL
6. Replace `YOUR_USERNAME` in this README with your HF username

---

## 💡 Example Questions to Try

```
What is the second law of thermodynamics?
Calculate the heat transfer: k=50 W/mK, A=2m², ΔT=30K, L=0.1m
What material should I use for a marine environment with high loads?
Explain how convolutional neural networks are used in quality inspection
What is the difference between ductile and brittle fracture?
How does a digital twin work in manufacturing?
Solve: A shaft of diameter 40mm transmits 20kW at 500rpm. Find the shear stress.
```

---

## 📊 System Architecture

```
User types question
        ↓
Streamlit chat interface
        ↓
Python backend (prompt engineering)
        ↓
Google Gemini API (AI model)
        ↓
Response parsed & displayed
        ↓
Chat history maintained in session
```

---

## 🔮 Future Scope

- [ ] PDF upload — ask questions about uploaded textbook chapters
- [ ] LaTeX formula rendering in chat
- [ ] Quiz / MCQ generator for exam prep
- [ ] Voice input support
- [ ] Hindi / Telugu / Tamil language support
- [ ] GATE exam question bank fine-tuning

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| [Your Name] | Developer & Project Lead |
| [Friend's Name] | Domain Expert (Mechanical Engineering) |

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">

**Built with Python + Streamlit + Google Gemini API**  
**Deployed free on Hugging Face Spaces**  
**Total cost: ₹0**

⭐ Star this repo if it helped you!

</div>
