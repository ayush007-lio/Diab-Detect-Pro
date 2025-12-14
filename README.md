<div align="center">

  <img src="https://img.icons8.com/external-flaticons-flat-flat-icons/100/external-diabetes-anatomy-flaticons-flat-flat-icons.png" alt="logo" width="100" height="100" />

  # 🩺 GlucoSense AI: Diabetes Prediction System
  
  **A Smart Healthcare Assistant powered by Machine Learning**

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-2.0-red?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-Library-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

  <p>
    <a href="#-about-the-project">About</a> •
    <a href="#-key-features">Features</a> •
    <a href="#-tech-stack">Tech Stack</a> •
    <a href="#-how-to-run">How to Run</a> •
    <a href="#-screenshots">Screenshots</a>
  </p>
</div>

---

## 🧐 About The Project

**GlucoSense AI** is an end-to-end Machine Learning web application designed to assist in the early detection of diabetes. 

By analyzing standard health metrics (like Glucose, BMI, Age, etc.), the Random Forest model predicts the likelihood of diabetes with high accuracy. The project wraps this powerful model in a beautiful, responsive user interface and offers instant **PDF Report Generation** for users to save their results.

## ✨ Key Features

* **🤖 High Accuracy ML Model:** Trained on the reliable Pima Indians Diabetes Dataset using Random Forest Classifier.
* **🎨 Modern UI/UX:** A clean, responsive interface built with CSS Gradients and Glassmorphism effects.
* **📄 PDF Report Generation:** Users can download a professional medical report of their prediction instantly.
* **⚡ Real-time Prediction:** Get results in milliseconds.
* **🔒 Data Persistence:** Input forms don't vanish after prediction, allowing for easy corrections.

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (html2pdf.js) |
| **Backend** | Python, Flask |
| **ML Engine** | Scikit-Learn, Pandas, NumPy |
| **Model** | Random Forest Classifier |

## 🚀 How to Run

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/GlucoSense-AI.git](https://github.com/your-username/GlucoSense-AI.git)
cd GlucoSense-AI
2. Create a Virtual Environment (Optional but Recommended)
Bash

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Train the Model
Run the training script to generate the model.pkl file.

Bash

python train_model.py
5. Run the Application
Bash

python app.py
Open your browser and navigate to: http://127.0.0.1:5000/

📂 Project Structure
Plaintext

GlucoSense-AI/
├── dataset/
│   └── diabetes.csv       # Pima Indians Diabetes Dataset
├── static/
│   └── style.css          # Modern styling for the UI
├── templates/
│   └── index.html         # Frontend HTML template
├── app.py                 # Flask Main Application
├── train_model.py         # ML Training Script
├── model.pkl              # Saved Machine Learning Model
└── requirements.txt       # Project Dependencies
