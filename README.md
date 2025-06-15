# TDS Virtual TA - Frontend 🎛️

A **lightweight Streamlit-based UI** for the `TDS Virtual TA` project.  
Ask questions and optionally upload images (e.g., lecture slides or screenshots) to get contextual answers.

> 🔗 **Main API & Backend Project:** [technosrijan/tds-virtual-ta](https://github.com/technosrijan/tds-virtual-ta)

---

## 🚀 Features

- Simple UI for asking text/image-based questions
- Calls the FastAPI backend deployed on Render
- Displays generated answers and relevant course links

---

## 🛠️ How to Run

1. **Clone this repo**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## 📦 Dependencies

- streamlit
- requests

---

## 🔗 Main Project Overview

The backend and core logic (OCR, embeddings, vector search, answer generation) is implemented in the main repository:

➡️ [technosrijan/tds-virtual-ta](https://github.com/technosrijan/tds-virtual-ta)

This frontend simply acts as a user-facing layer over that API.

---

## 📝 License

MIT License — feel free to use