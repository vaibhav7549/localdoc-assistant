# app.py - LocalDoc Assistant
# A private AI document reader that runs 100% locally

import streamlit as st
import ollama
import PyPDF2

# --- Page setup ---
st.set_page_config(page_title="LocalDoc Assistant", page_icon="🔒")
st.title("🔒 LocalDoc Assistant")
st.caption("Your documents never leave this computer. Powered by open-source AI.")

# --- Sidebar: Privacy dashboard ---
with st.sidebar:
    st.header("🔐 Privacy Dashboard")
    st.success("✅ Local processing only")
    st.success("✅ No internet connection used")
    st.success("✅ No data sent to any server")
    st.info("Model: Gemma 2 (2B) via Ollama")

# --- File uploader ---
uploaded_file = st.file_uploader(
    "Upload a document (PDF or TXT)",
    type=["pdf", "txt"]
)

# --- Function to extract text from uploaded file ---
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        return file.read().decode("utf-8")

# --- Main logic ---
if uploaded_file is not None:
    document_text = extract_text(uploaded_file)
    
    st.subheader("📄 Document Preview")
    st.text_area("Extracted text", document_text[:2000] + "...", height=150)
    
    context = document_text[:6000]
    
    st.subheader("❓ Ask a question about this document")
    question = st.text_input("Your question:", placeholder="e.g., What is the total amount? Who signed this?")
    
    if st.button("Ask AI") and question:
        with st.spinner("Thinking locally... (this runs on your computer)"):
            prompt = f"""You are a helpful assistant. Answer the question based ONLY on the document below.
If the answer is not in the document, say "I could not find that in the document."

DOCUMENT:
{context}

QUESTION: {question}

ANSWER:"""
            
            response = ollama.chat(
                model="gemma2:2b",
                messages=[{"role": "user", "content": prompt}]
            )
            
            st.subheader("🤖 AI Answer")
            st.write(response["message"]["content"])
            
            st.caption("This answer was generated entirely on your computer. No data was sent anywhere.")

else:
    st.info("👆 Upload a document to get started.")