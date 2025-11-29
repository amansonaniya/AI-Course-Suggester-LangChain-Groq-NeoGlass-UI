# 📘 **AI Course Suggester – LangChain + Groq + NeoGlass UI**

An intelligent AI-powered system that generates a **personalized learning roadmap** based on your current skills, skills you want to learn, career goal, and available learning duration.

This project uses:

✅ **LangChain** for prompt management + LLM orchestration
✅ **Groq LLaMA 3.1 8B Instant** for fast and accurate generation
✅ **Strict JSON output** for easy frontend rendering
✅ **NeoGlass modern UI** with dark/light modes, animations, navbar, and footer
✅ **FastAPI backend** + simple HTML/CSS/JS frontend

---

## 🚀 **Features**

* Personalized **course recommendations** (5 courses)
* Each course includes:

  * Title
  * Objective
  * Recommended platforms
* **3-phase roadmap** automatically generated
* **Expert notes/tips**
* Clean JSON structure
* **Copy / Download JSON** buttons
* NeoGlass animated UI
* Dark/Light mode toggle
* Responsive design
* 100% local or deployable to Render + Netlify

---

## 🧠 **Tech Stack**

### **Backend**

* FastAPI
* LangChain
* Groq API (LLaMA 3.1–8B Instant)
* Python 3.10–3.12

### **Frontend**

* HTML5
* CSS3 (NeoGlass theme + animations)
* Vanilla JavaScript
* Fetch API

---

## 📂 **Project Structure**

```
ai-course-suggester/
│── backend/
│     ├── app.py
│     ├── langchain_helper.py
│     ├── secret_key.py
│── frontend/
│     ├── index.html
│     ├── styles.css
│     ├── favicon.svg
│── requirements.txt
│── README.md
```

---

## 🔧 **Setup Instructions (Local)**

### **1. Install Python**

Use Python 3.10 – 3.12
Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### **2. Create and activate a virtual environment**

```
python -m venv venv
venv\Scripts\activate    (Windows)
source venv/bin/activate (Mac/Linux)
```

---

### **3. Install dependencies**

```
pip install -r requirements.txt
```

---

### **4. Add your Groq API key**

Open:

```
backend/secret_key.py
```

Paste your key:

```python
groq_api_key = "gsk_yourkey_here"
```

---

### **5. Run backend server**

```
uvicorn backend.app:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

### **6. Run frontend**

Open file:

```
frontend/index.html
```

(No server needed — pure HTML/JS)

---

## 🧩 **How It Works (LangChain Workflow)**

### ✔ Input values from UI:

* Skills known
* Skills to learn
* Career goal
* Duration (months)

### ✔ LangChain PromptTemplate

A structured prompt is used to request **strict JSON output**, including:

* 5 course objects
* 3-phase roadmap
* Notes

### ✔ Groq LLaMA Model

Fast JSON generation using:

```
llama-3.1-8b-instant
```

### ✔ Output Parser

`StrOutputParser()` captures raw LLM-output → parsed with Python `json.loads`.

### ✔ Frontend Rendering

Styled cards display:

* Courses
* Platforms
* Roadmap
* Notes

Includes:

* Dark mode
* Copy to clipboard
* Download JSON
* Animated loader

---

## 🧪 **API Endpoint**

### **POST /generate**

**Request Body**

```json
{
  "skills_known": "Python, SQL",
  "skills_want": "Machine Learning",
  "career_goal": "Data Scientist",
  "duration_months": 6
}
```

**Response**

```json
{
  "success": true,
  "data": {
    "courses": [...],
    "roadmap": {...},
    "notes": "..."
  }
}
```

---

## 🌍 **Deployment Guide**

### 🚀 **Deploy Backend (Render)**

1. Create a new Render Web Service
2. Use Python environment
3. Add environment variable:

   ```
   GROQ_API_KEY=your_key
   ```
4. Start command:

   ```
   uvicorn backend.app:app --host 0.0.0.0 --port 10000
   ```
5. Deploy

---

### 🌐 **Deploy Frontend (Netlify)**

1. Open Netlify → “Deploy site”
2. Drag & drop the **frontend** folder
3. Done (static hosting)

---

## ✔️ **Screenshots (if needed)**

I can generate screenshot-ready templates.

---

## 📝 **Remarks**

This project demonstrates:

* Clean prompt engineering
* LangChain workflow design
* JSON-structured LLM responses
* Full-stack AI application development
* Groq integration
* Modern UI + fully responsive design

It is a complete production-ready AI app that converts user inputs into a smart career roadmap.
 
