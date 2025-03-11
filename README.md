# 📊 CSV Question Answering & Visualization (Gradio + FastAPI + Ollama)

## 📝 Project Overview
This project is a Gradio-based web application that allows users to:
1. Upload CSV files 📂
2. Ask questions about the data using a local LLM (Llama 3.2 via Ollama) 🧠
3. Generate visualizations 📊

The backend is built using FastAPI with Polars for data handling, while the frontend is implemented using Gradio.

---

## 🚀 Features
✅ Upload and validate CSV files (max size: **25MB**)
✅ Answer textual and numerical queries about CSV data using Ollama LLM
✅ Generate Bar & Line Graphs for selected columns
✅ Modular design with FastAPI, Gradio, and Polars for efficiency

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
git clone https://github.com/theharshdadhich/CSV-insight.git
cd CSV-insight

### 2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # Install dependencies

### 3️⃣ Install and Run Ollama (for LLM processing)
ollama pull llama3.2  # Download Llama 3.2 
ollama serve  # Start Ollama server

### 4️⃣ Run the FastAPI Backend
uvicorn main:app --reload
📌 Access FastAPI API Docs: http://127.0.0.1:8000/docs

### 5️⃣ Run the Gradio Frontend
python app.py
📌 Access Gradio UI: http://127.0.0.1:7860 (http://127.0.0.1:7860/)

---

## 🔌 API Endpoints
| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | /upload/            | Upload a CSV file            |
| POST   | /ask/               | Ask a question to LLM        |
| POST   | /plot/              | Generate a graph from CSV    |

---

## 📸 Screenshots
File Upload:-
![image](https://github.com/user-attachments/assets/1f03164f-9aec-45f0-87db-a0d2c95bb5fa)
Ask Question:-
![image](https://github.com/user-attachments/assets/d1f35f48-54e5-4671-ada1-bbf54d902fa8)
Plot Graph:-
![image](https://github.com/user-attachments/assets/6547d4f6-10db-4a3e-a19d-8bcf4c96308e)



---

## 🎯 Future Improvements
- 🔹 Support more graph types (scatter, histogram, etc.)
- 🔹 Improve error handling & validation
- 🔹 Optimize LLM processing for better performance
- 🔹 Add frontend UI improvements for a better user experience

---

## 📝 License
This project is open-source under the MIT License.

---

## ✉️ Contact
For questions, reach out via harshdadhich1109@gmail.com or open an issue on GitHub! 🚀
