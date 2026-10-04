# LocalDoc Assistant

A private AI document assistant that runs 100% offline. Upload a PDF or TXT file, ask questions about it, and get answers — all without any data leaving your computer.

Built for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01).

## Why

My friend is a freelance lawyer who handles sensitive client contracts. She can't upload them to cloud AI services for confidentiality reasons. This tool gives her AI-powered document search with complete privacy.

## Tech Stack

- **Ollama** — local LLM runtime
- **Gemma 2 (2B)** — Google's open-weight model
- **Streamlit** — Python web UI
- **PyPDF2** — PDF text extraction

## How to Run

1. Install [Ollama](https://ollama.com/download)
2. `ollama pull gemma2:2b`
3. `pip install streamlit ollama PyPDF2`
4. `python -m streamlit run app.py`

## License

MIT