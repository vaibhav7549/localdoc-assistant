# 🔒 LocalDoc Assistant

A private AI document assistant that runs **100% offline**. Upload a PDF or TXT file, ask questions about it, and get answers — all without any data leaving your computer.

Built for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01).

## Why I Built This

My friend is a freelance lawyer who handles sensitive client contracts. She wanted to use AI to quickly find information in long documents, but she couldn't upload them to ChatGPT or other cloud services because of confidentiality rules.

LocalDoc Assistant gives her AI-powered document search with **complete privacy**. Her data never leaves her laptop.

## Features

- ✅ **100% offline** — no internet required after setup
- ✅ **Privacy-first** — no data sent to any server
- ✅ **Free to run** — no API keys, no subscriptions
- ✅ **PDF and TXT support**
- ✅ **Open-source AI** — powered by Google's Gemma 2

## Tech Stack

| Component | Purpose |
|-----------|---------|
| [Ollama](https://ollama.com) | Local LLM runtime |
| [Gemma 2 (2B)](https://ai.google.dev/gemma) | Google's open-weight model |
| [Streamlit](https://streamlit.io) | Python web UI |
| [PyPDF2](https://pypi.org/project/PyPDF2/) | PDF text extraction |

## How to Run

### 1. Install Ollama
Download from [ollama.com/download](https://ollama.com/download) and install.

### 2. Download the model
```bash
ollama pull gemma2:2b
