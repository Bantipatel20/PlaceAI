# Placement Prediction Web App

This project is a **Flask-based web application** that predicts **whether a student will get placed or not** based on their **CGPA and IQ Score**. It uses a **Machine Learning model** (Logistic Regression) to make predictions.

---

## 🚀 Features

- 📊 **Predicts placement status** using CGPA and IQ
- 🌐 **Web interface** for easy input and result display
- 🏗️ **Built with Flask, HTML, and CSS**
- 🎯 **Deployable on platforms like Heroku, Render, or AWS**

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Flask (Python)
- **Machine Learning Model:** Logistic Regression (Pickle File)
- **Deployment:** Heroku / Render / AWS

---

## 📂 Project Structure

```
📦 Placement Prediction
├── app.py              # Main Flask application
├── model.pkl           # Trained ML model
├── templates
│   ├── index.html      # Frontend HTML template
├── static
│   ├── styles.css      # (Optional) CSS file for styling
├── README.md           # Documentation
├── requirements.txt    # Dependencies
```

---

## 🔥 Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Flask App

```bash
python app.py
```

**App will run at:** `http://127.0.0.1:8080/`

### 3️⃣ Deploy on Heroku (Optional)

```bash
heroku create my-placement-app
heroku git:remote -a my-placement-app
git push heroku main
```

---

## 📌 Usage

1. **Enter CGPA and IQ Score** in the web interface.
2. Click on **Predict Placement**.
3. **Model will predict** whether placement is possible.

---

## 📜 License

This project is **open-source** and free to use.

---

## 💡 Author

Developed by **Banti Patel** 🚀
