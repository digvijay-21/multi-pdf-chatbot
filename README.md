# 📚 Multi-PDF Chatbot with Firebase Auth + LangChain 🤖

This is a clean AI-powered chatbot built using **Streamlit**, **LangChain**, and **Firebase Authentication**. It allows users to:

- Upload multiple PDF files 📄
- Ask natural language questions 🤔
- Get intelligent, context-aware answers powered by LLMs 🧠


---

## 🚀 Features

✅ Upload & process multiple PDFs  
✅ Ask context-based questions to your documents  
✅ Firebase Email/Password login & signup  
✅ Fast PDF chunking and vector embedding (FAISS)  
✅ LLM integration using OpenAI and HuggingFace  
✅ Clean, minimal UI with Streamlit

---

## 🧑‍💻 Tech Stack

| Layer       | Technology             |
|------------|------------------------|
| Frontend   | Streamlit              |
| LLM        | LangChain + OpenAI, HuggingFace     |
| Vector DB  | FAISS                  |
| PDF Parser | PyPDF2                 |
| Auth       | Firebase Auth (REST)   |
| Hosting    | Streamlit Community Cloud |

---

## 🧳 Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/digvijay-21/multi-pdf-chatbot.git
cd multi-pdf-chatbot
```

### 2. Add Firebase Configuration

1. Go to your [Firebase Console](https://console.firebase.google.com/)
2. Create a new project (if not already done)
3. Enable **Email/Password Authentication** under `Authentication > Sign-in method`
4. Generate a **Web API key** from `Project Settings > General`
5. Create a **service account** (Admin SDK) and download the JSON file as `serviceAccountKey.json`
6. Create a `.env` file in your project root:

```env
FIREBASE_API_KEY=your_web_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 Tip: Use a virtual environment if you're working locally.

### 4. Run the App

```bash
streamlit run app.py
```

You’ll see a browser window open with the chatbot interface.

---

## 📁 Project Structure

```
multi-pdf-chatbot/
├── app.py                  ← Main Streamlit app
├── htmlTemplates.py        ← Templates for chat bubbles
├── .env                    ← Environment variables (API key)
├── requirements.txt        ← Python dependencies
├── .gitignore              ← Files to ignore in Git
├── serviceAccountKey.json  ← Firebase Admin SDK
├── architecture.jpg     ← Visual architecture or sequence diagram
└── README.md
```

---

## ⚠️ Important Notes

- You **only use Firebase for authentication** — no Firestore or message history is saved
- Uploaded PDFs and chat context exist **only in the user's session memory**
- You must have an OpenAI key set up via LangChain to use the chatbot

---

## 🌐 Deployment

Want to share your app publicly? You can deploy it to:

### 📦 Streamlit Cloud

1. Push your code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Set secrets in the dashboard for:

```
FIREBASE_API_KEY=your_key
```

5. Upload `serviceAccountKey.json` using `st.secrets` or ignore if not using Firestore

### 📍 Live Demo

**Working App:** [https://multi-pdf-chatbot.streamlit.app](https://multi-pdf-chatbot.streamlit.app)  
> Feel free to test the features and explore!

### 📄 App Architecture

Here is a high-level architecture of the project:

![App Flow](architecture.jpg)

---

## 🙌 Acknowledgements

- [LangChain](https://langchain.com/)
- [Firebase](https://firebase.google.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://platform.openai.com/) / [HuggingFace](https://huggingface.co/)

---

## 📬 Contact

**Made by [Digvijay Bhongale](https://github.com/digvijay-21)**  
If you liked the project, drop a ⭐️ and share!

---
