<div align="center">

# 🔒 LocalDoc Assistant

### *Your documents. Your AI. Your computer. Nobody else's.*

A private AI document assistant that runs **100% offline**.
Upload a PDF or TXT file, ask questions about it, and get answers —
**without a single byte leaving your computer.**

<br />

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![Gemma 2](https://img.shields.io/badge/Gemma_2-4285F4?style=flat-square&logo=google&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Open Source](https://img.shields.io/badge/Open_Source-❤️-red?style=flat-square)

<br />

[💡 Why](#-why-i-built-this) · [✨ Features](#-features) · [🎬 Demo](#-demo) · [🚀 Run It](#-how-to-run) · [🌍 Open AI](#-why-open-innovation-matters) · [🎃 Hacktoberfest](#-hacktoberfest-2026)

</div>

---

## 💡 Why I Built This

> *"I can't upload client contracts to ChatGPT. It's a confidentiality thing."*
>
> — **My friend, a freelance lawyer**

My friend handles sensitive legal documents every day. She wanted AI to help her find information faster — but every cloud AI service meant sending confidential data to a server she doesn't control.

So I built her something better.

**LocalDoc Assistant** gives her AI-powered document search with **complete privacy**. The AI runs on her laptop. Nothing goes to the internet. Nothing gets logged. Nothing gets trained on. Just her, her documents, and an open-source model that respects both.

```
   ┌───────────────────────────────────────────────────────┐
   │  🔒 Her documents → 🧠 Her laptop's AI → 💬 Answer     │
   │                                                       │
   │         ☁️  NOTHING EVER TOUCHES THE CLOUD  ☁️         │
   └───────────────────────────────────────────────────────┘
```

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Radically Private
Your documents never leave your machine. No servers. No tracking. No telemetry.

</td>
<td width="50%" valign="top">

### ⚡ Blazing Fast
Runs locally with Gemma 2 — no waiting on network round trips to a cloud API.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💸 Free Forever
No API keys. No subscriptions. No per-token costs. Ever.

</td>
<td width="50%" valign="top">

### 📄 PDF & TXT Support
Drop in contracts, notes, medical records, study material — anything text-based.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧠 Open-Weight AI
Powered by Google's Gemma 2. Swap it for any other model in one line.

</td>
<td width="50%" valign="top">

### 🎨 Simple UI
Built with Streamlit — clean, instant, and no setup for the person using it.

</td>
</tr>
</table>

---

## 🎬 Demo

<div align="center">

<img src="demo.png" alt="LocalDoc Assistant demo" width="800" />

*The app correctly answers **"March 15, 1995"** from an uploaded text file — offline.*

</div>

---

## 🧰 Tech Stack

<div align="center">

| 🧩 Layer | 🛠️ Tool | 🎯 Purpose |
|:--------:|:-------:|:----------|
| **AI Runtime** | [Ollama](https://ollama.com) | Runs LLMs locally on any machine |
| **Model** | [Gemma 2 (2B)](https://ai.google.dev/gemma) | Google's open-weight model |
| **UI** | [Streamlit](https://streamlit.io) | Instant web interface in Python |
| **PDF Parsing** | [PyPDF2](https://pypi.org/project/PyPDF2/) | Extracts text from PDFs |
| **Language** | Python 3.9+ | Glues it all together |

</div>

---

## 🚀 How to Run

### 1️⃣ Install Ollama
Download from **[ollama.com/download](https://ollama.com/download)** and install it.

### 2️⃣ Download the model
```bash
ollama pull gemma2:2b
```

### 3️⃣ Get the code
Click the green **Code** button above → **Download ZIP** → extract it.

*(Or, if you have Git:* `git clone https://github.com/vaibhav7549/localdoc-assistant.git`*)*

### 4️⃣ Install Python dependencies
```bash
pip install streamlit ollama PyPDF2
```

### 5️⃣ Run the app
```bash
python -m streamlit run app.py
```

The browser opens at `http://localhost:8501`. The first query may take 10–20 seconds while the model loads into memory. After that, it's instant.

---

## 🕹️ How to Use

```
┌─────────────────────────────────────────────┐
│  1.  📄  Upload a PDF or TXT file           │
│  2.  ❓  Ask a question about the document   │
│  3.  🤖  Click "Ask AI"                      │
│  4.  ✅  Read the answer — 100% locally      │
└─────────────────────────────────────────────┘
```

---

## 🌍 Why Open Innovation Matters

This project would be **impossible** with a closed API.

The entire point is privacy — my friend *cannot* upload client documents to a third-party server. Open-source AI was the only way.

<div align="center">

| 🔒 Closed API | 🔓 Open-Source AI *(what I chose)* |
|:-------------|:----------------------------------|
| Data leaves your machine | Data **never leaves your machine** |
| Pay per token, forever | **Free** to run, forever |
| Fixed model, fixed behavior | **Swap models** with one line of code |
| Company can change terms overnight | **You own the stack** |
| Requires internet | **Works offline** |

</div>

Open innovation means the tool answers to the person using it — not the other way around.

---

## 📁 Project Structure

```
localdoc-assistant/
│
├── 📄  app.py            # The Streamlit app + Ollama integration
├── 📘  README.md         # You are here
├── 🖼️  demo.png          # Screenshot of the app in action
├── ⚖️  LICENSE           # MIT — free to use, modify, share
└── 🚫  .gitignore        # Keeps venv/ out of the repo
```

---

## 🎃 Hacktoberfest 2026

This project was built for the **[Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)** on DEV Community.

<div align="center">

![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2026-FF6B35?style=for-the-badge&logo=hacktoberfest&logoColor=white)
![Challenge](https://img.shields.io/badge/Challenge-Weekend_·_Build_for_a_Friend-9B59B6?style=for-the-badge)
![Category](https://img.shields.io/badge/Prize_Category-Best_Use_of_Gemma-4285F4?style=for-the-badge&logo=google&logoColor=white)

<br />

| | |
|:---:|:---:|
| **Theme** | Build for a Friend |
| **Category** | Best Use of Gemma |
| **Write-up** | [Read it on DEV →](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01) |

</div>

---

## 🤝 Contributing

Ideas, bug reports, and pull requests are welcome.

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-idea`
3. Commit: `git commit -m "Add your idea"`
4. Push: `git push origin feature/your-idea`
5. Open a Pull Request

---

## 📜 License

Released under the **MIT License** — see [LICENSE](LICENSE).

You're free to use, modify, distribute, and even sell it. Just keep the copyright notice.

---

<div align="center">

### ⭐ If this helped you, drop a star — it means a lot!

<br />

**Built with ❤️ for a friend who deserves better than the cloud.**

<br />

<a href="https://github.com/vaibhav7549/localdoc-assistant/stargazers">
  <img src="https://img.shields.io/github/stars/vaibhav7549/localdoc-assistant?style=social" alt="Stars" />
</a>
<a href="https://github.com/vaibhav7549/localdoc-assistant/network/members">
  <img src="https://img.shields.io/github/forks/vaibhav7549/localdoc-assistant?style=social" alt="Forks" />
</a>

<br /><br />

<sub>Made with ❤️ and open-source AI · © 2026 Vaibhav</sub>

</div>
