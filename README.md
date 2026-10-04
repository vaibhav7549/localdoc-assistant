<!-- ═══════════════════════════════════════════════════════════
     🔒  LocalDoc Assistant
     Private AI document Q&A — 100% offline
     ═══════════════════════════════════════════════════════════ -->

<div align="center">

<br />

# 🔒 LocalDoc Assistant

### *Your documents. Your AI. Your computer. Nobody else's.*

<br />

A private AI document assistant that runs **100% offline**.
Upload a PDF or TXT file, ask questions about it, and get answers —
**without a single byte leaving your computer.**

<br />

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Gemma 2](https://img.shields.io/badge/Gemma_2-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)

[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](https://github.com/vaibhav7549/localdoc-assistant/pulls)
[![Made with Love](https://img.shields.io/badge/Made_with-❤️_for_a_friend-ff69b4?style=for-the-badge)](https://github.com/vaibhav7549)

<br />

```
  🔒   ────   🧠   ────   💬
 File      Local AI      Answer
```

### [💡 Why](#-why-i-built-this) · [✨ Features](#-features) · [🎬 Demo](#-demo) · [🚀 Quick Start](#-quick-start) · [🌍 Open AI](#-why-open-innovation-matters) · [🎃 Hacktoberfest](#-hacktoberfest-2026)

<br />

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 💡 Why I Built This

</div>

> [!IMPORTANT]
> *"I can't upload client contracts to ChatGPT. It's a confidentiality thing."*
>
> — **A friend who works with sensitive documents**

A friend handles confidential documents every day. They wanted AI to help find information faster — but every cloud AI service meant sending private data to a server they don't control.

So I built them something better.

**LocalDoc Assistant** gives them AI-powered document search with **complete privacy**. The AI runs on their laptop. Nothing goes to the internet. Nothing gets logged. Nothing gets trained on. Just them, their documents, and an open-source model that respects both.

<div align="center">

```
   ┌──────────────────────────────────────────────────────────┐
   │                                                          │
   │    📄  Their document  ──►  🧠  Their laptop's AI  ──►  💬  │
   │                                                          │
   │           ☁️   NOTHING EVER TOUCHES THE CLOUD   ☁️         │
   │                                                          │
   └──────────────────────────────────────────────────────────┘
```

</div>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## ✨ Features

</div>

<table>
<tr>
<td width="33.33%" align="center" valign="top">

<br />

### 🔐

**Radically Private**

Your documents never leave your machine. No servers. No tracking. No telemetry.

<br />

</td>
<td width="33.33%" align="center" valign="top">

<br />

### ⚡

**Blazing Fast**

Runs locally with Gemma 2 — no waiting on network round trips to a distant cloud.

<br />

</td>
<td width="33.33%" align="center" valign="top">

<br />

### 💸

**Free Forever**

No API keys. No subscriptions. No per-token costs. Ever.

<br />

</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">

<br />

### 📄

**PDF & TXT Support**

Contracts, notes, medical records, study material — anything text-based.

<br />

</td>
<td width="33.33%" align="center" valign="top">

<br />

### 🧠

**Open-Weight AI**

Powered by Google's Gemma 2. Swap for any other model in one line.

<br />

</td>
<td width="33.33%" align="center" valign="top">

<br />

### 🎨

**Simple UI**

Built with Streamlit — clean, instant, and zero setup for the person using it.

<br />

</td>
</tr>
</table>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🎬 Demo

<br />

<img src="demo.png" alt="LocalDoc Assistant answering a question about an uploaded document" width="820" />

<br /><br />

*The app correctly answers* ***"March 15, 1995"*** *from an uploaded text file — offline.*

<br />

</div>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🧰 Tech Stack

</div>

<div align="center">

| &nbsp;&nbsp;🧩 Layer&nbsp;&nbsp; | &nbsp;&nbsp;🛠️ Tool&nbsp;&nbsp; | &nbsp;&nbsp;🎯 Purpose&nbsp;&nbsp; |
|:---:|:---:|:---|
| **AI Runtime** | [**Ollama**](https://ollama.com) | Runs LLMs locally on any machine |
| **Model** | [**Gemma 2 (2B)**](https://ai.google.dev/gemma) | Google's open-weight model |
| **UI** | [**Streamlit**](https://streamlit.io) | Instant web interface in Python |
| **PDF Parsing** | [**PyPDF2**](https://pypi.org/project/PyPDF2/) | Extracts text from PDFs |
| **Language** | [**Python 3.9+**](https://python.org) | Glues it all together |

</div>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🚀 Quick Start

### *From zero to running in under 5 minutes*

</div>

<br />

### **1️⃣ &nbsp; Install Ollama**

Download from **[ollama.com/download](https://ollama.com/download)** and install it.

<br />

### **2️⃣ &nbsp; Download the model**

```bash
ollama pull gemma2:2b
```

<br />

### **3️⃣ &nbsp; Get the code**

Click the green **`Code`** button at the top of this page → **Download ZIP** → extract.

<details>
<summary><i>Or, if you prefer Git, click here</i></summary>
<br />

```bash
git clone https://github.com/vaibhav7549/localdoc-assistant.git
cd localdoc-assistant
```

</details>

<br />

### **4️⃣ &nbsp; Install Python dependencies**

```bash
pip install streamlit ollama PyPDF2
```

<br />

### **5️⃣ &nbsp; Run the app**

```bash
python -m streamlit run app.py
```

<br />

> [!TIP]
> The browser opens at **`http://localhost:8501`**. The first query may take 10–20 seconds while the model loads into memory. After that, it's instant.

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🕹️ How to Use

<br />

```
   ┌───────────────────────────────────────────────┐
   │                                               │
   │    1.   📄   Upload a PDF or TXT file         │
   │                                               │
   │    2.   ❓   Ask a question about it           │
   │                                               │
   │    3.   🤖   Click  " Ask AI "                 │
   │                                               │
   │    4.   ✅   Read the answer — 100% locally    │
   │                                               │
   └───────────────────────────────────────────────┘
```

</div>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🌍 Why Open Innovation Matters

</div>

This project would be **impossible** with a closed API. The entire point is privacy — my friend *cannot* upload confidential documents to a third-party server. Open-source AI was the only way.

<div align="center">

| 🔒 &nbsp; **Closed API** | 🔓 &nbsp; **Open-Source AI** *(what I chose)* |
|:---|:---|
| Data leaves your machine | Data **never leaves your machine** |
| Pay per token, forever | **Free** to run, forever |
| Fixed model, fixed behavior | **Swap models** with one line of code |
| Company can change terms overnight | **You own the stack** |
| Requires internet | **Works offline** |

</div>

<br />

> [!NOTE]
> **Open innovation means the tool answers to the person using it — not the other way around.**

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 📁 Project Structure

</div>

```
localdoc-assistant/
│
├── 📄  app.py            →  The Streamlit app + Ollama integration
├── 📘  README.md         →  You are here
├── 🖼️  demo.png          →  Screenshot of the app in action
├── ⚖️  LICENSE           →  MIT — free to use, modify, share
└── 🚫  .gitignore        →  Keeps venv/ out of the repo
```

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🎃 Hacktoberfest 2026

</div>

<div align="center">

![Hacktoberfest](https://img.shields.io/badge/🎃_Hacktoberfest-2026-FF6B35?style=for-the-badge)
![Theme](https://img.shields.io/badge/Theme-Build_for_a_Friend-9B59B6?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Best_Use_of_Gemma-4285F4?style=for-the-badge&logo=google&logoColor=white)

<br />

*This project was built for the **[Hacktoberfest Weekend Challenge](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)** on DEV Community.*

</div>

<br />

<details>
<summary><b>📋 &nbsp; Challenge details (click to expand)</b></summary>

<br />

| | |
|:---|:---|
| **🎃 Event** | Hacktoberfest 2026 |
| **🏆 Challenge** | Weekend Challenge |
| **🎨 Theme** | Build for a Friend |
| **🥇 Category** | Best Use of Gemma |
| **📝 Write-up** | [Read it on DEV →](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01) |
| **🧠 Model** | Google's Gemma 2 (open-weight) |
| **🔒 Approach** | Fully local, fully offline |

</details>

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 🤝 Contributing

</div>

Ideas, bug reports, and pull requests are welcome.

```bash
# 1. Fork the repo
# 2. Create your branch
git checkout -b feature/your-idea

# 3. Make your changes and commit
git commit -m "Add your idea"

# 4. Push and open a Pull Request
git push origin feature/your-idea
```

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br />

<div align="center">

## 📜 License

</div>

Released under the **MIT License** — see [LICENSE](LICENSE) for details.

You're free to use, modify, distribute, and even sell it. Just keep the copyright notice.

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

<br /><br />

<div align="center">

## ⭐ If this helped you, drop a star — it means a lot!

<br />

### *Built with ❤️ for a friend who deserves better than the cloud.*

<br />

[![Stars](https://img.shields.io/github/stars/vaibhav7549/localdoc-assistant?style=for-the-badge&logo=github&label=Stars&color=yellow)](https://github.com/vaibhav7549/localdoc-assistant/stargazers)
[![Forks](https://img.shields.io/github/forks/vaibhav7549/localdoc-assistant?style=for-the-badge&logo=github&label=Forks&color=blue)](https://github.com/vaibhav7549/localdoc-assistant/network/members)
[![Issues](https://img.shields.io/github/issues/vaibhav7549/localdoc-assistant?style=for-the-badge&logo=github&label=Issues&color=red)](https://github.com/vaibhav7549/localdoc-assistant/issues)

<br /><br />

```
     ╔═══════════════════════════════════════════════════════╗
     ║                                                       ║
     ║          🎃   Happy Hacktoberfest 2026   🎃            ║
     ║                                                       ║
     ║      "The best AI is the one that answers to you,     ║
     ║              not to a server."                        ║
     ║                                                       ║
     ╚═══════════════════════════════════════════════════════╝
```

<br />

<sub>Made with ❤️ and open-source AI · © 2026 Vaibhav</sub>

<br /><br />

</div>
