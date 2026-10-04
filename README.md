# 🔒 LocalDoc Assistant

A private AI document assistant that runs **100% offline**. Upload a PDF or TXT file, ask questions about it, and get answers — all without any data leaving your computer.

Built for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01).

![Demo](demo.png)

---

## Why I Built This

My friend is a freelance lawyer who handles sensitive client contracts. She wanted to use AI to quickly find information in long documents, but she couldn't upload them to ChatGPT or other cloud services because of confidentiality rules.

LocalDoc Assistant gives her AI-powered document search with **complete privacy**. Her data never leaves her laptop.

---

## Features

- ✅ **100% offline** — no internet required after setup
- ✅ **Privacy-first** — no data sent to any server
- ✅ **Free to run** — no API keys, no subscriptions
- ✅ **PDF and TXT support**
- ✅ **Open-source AI** — powered by Google's Gemma 2

---

## Tech Stack

| Component | Purpose |
|-----------|---------|
| [Ollama](https://ollama.com) | Local LLM runtime |
| [Gemma 2 (2B)](https://ai.google.dev/gemma) | Google's open-weight model |
| [Streamlit](https://streamlit.io) | Python web UI |
| [PyPDF2](https://pypi.org/project/PyPDF2/) | PDF text extraction |

---

## How to Run

### 1. Install Ollama
Download from [ollama.com/download](https://ollama.com/download) and install.

### 2. Download the model
```bash
ollama pull gemma2:2b
```

### 3. Get the code
Download this repo as a ZIP (green **Code** button → **Download ZIP**) and extract it, or use GitHub Desktop.

### 4. Install Python dependencies
```bash
pip install streamlit ollama PyPDF2
```

### 5. Run the app
```bash
python -m streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## How to Use

1. Upload a PDF or TXT file
2. Type a question about the document
3. Click **Ask AI**
4. Get your answer — generated entirely on your computer

---

## Why Open Innovation Matters

This project would be impossible with a closed API. The whole point is privacy — my friend cannot upload client documents to a third-party server. Open-source AI made this possible because:

- **Privacy:** The model runs locally. No data is transmitted anywhere.
- **Zero cost:** No API subscriptions or per-token fees.
- **Customizable:** She can swap in a larger model later if she needs better accuracy, without changing any code.

---

## License

MIT — see [LICENSE](LICENSE)
