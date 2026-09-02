# Autonomous AI Web (Browser-Use & LangChain)

An autonomous agent framework capable of navigating dynamic web applications, authenticating, filling forms, and validating complex visual UI states using LLMs (OpenAI & Groq / LLaMA-3).

## 🚀 Key Features
- **Hierarchical LLM Architecture**: Uses cost-effective fast models (Groq LLaMA-3) for planning/extraction and frontier LLMs for multi-step reasoning.
- **Dynamic DOM Navigation**: Interacts naturally with dynamic elements, dropdowns, buttons, and single-page apps.
- **Visual Proof Capture**: Automatically verifies completed tasks and captures full-page visual proof.
- **Resilient Execution**: Self-healing navigation with automatic retry strategies on UI state changes.

## 🛠️ Tech Stack
- **Frameworks**: LangChain, Browser-Use
- **Models**: OpenAI GPT-4o / GPT-3.5, Groq LLaMA-3 / Gemma
- **Async Runtime**: Python Asyncio

## 📦 Installation
```bash
git clone https://github.com/<your-username>/Agentic-Browser-Automation-AI.git
cd Agentic-Browser-Automation-AI
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and enter your API keys
python main.py
```

## 📄 License
MIT License
