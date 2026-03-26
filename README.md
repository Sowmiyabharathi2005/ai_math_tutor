# 📘 AI Math Tutor

An intelligent AI-powered system that solves algebra problems from images and provides step-by-step explanations with mistake detection.

---

## 📌 Project Overview

AI Math Tutor is a smart educational tool that helps students solve algebraic equations easily by using Artificial Intelligence.
It allows users to upload an image of a handwritten or printed math problem and automatically:

* Extracts the equation using OCR
* Converts it into a structured format
* Solves the equation using symbolic computation
* Displays detailed step-by-step solutions
* Detects common mistakes and provides feedback

This project bridges the gap between traditional learning and modern AI-based education.

---

## 🚀 Features

✅ Image-based algebra problem recognition
✅ Automatic equation extraction (OCR)
✅ LaTeX equation rendering
✅ Step-by-step solution generation
✅ Mistake detection and feedback
✅ Clean and interactive user interface
✅ Fast and accurate computation

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS / Streamlit
* **Backend**: Python (Flask / Streamlit)
* **Libraries**:

  * SymPy (Symbolic Mathematics)
  * OpenCV (Image Processing)
  * Tesseract OCR / EasyOCR
  * Pillow, NumPy
  * Python-dotenv
* **AI Integration**:

  * Gemini AI (for LaTeX and reasoning)

---

## 📂 Project Structure

```
ai_math_tutor/
│
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
│
├── services/
├── utils/
├── templates/
├── static/
│
├── uploads/
├── outputs/
└── logs/
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/yourusername/ai_math_tutor.git
cd ai_math_tutor
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Live Demo

https://ai-math-tutor.onrender.com

---

## 📷 Screenshots

👉 Add screenshots of:

* Upload page
* Solution page
* Output results

---

## 🧠 How It Works

1. User uploads an image
2. Image is preprocessed using OpenCV
3. OCR extracts mathematical text
4. Text is cleaned and converted to equation
5. Equation is solved using SymPy
6. Step-by-step explanation is generated
7. Mistakes are detected and displayed

---

## ⚠️ Limitations

* OCR accuracy depends on image quality
* Complex equations may require improvement
* Cloud deployment may not fully support OCR

---

## 🚀 Future Enhancements

* Multi-subject support (Physics, Chemistry)
* Advanced AI-based tutoring
* Personalized learning paths
* Voice input support
* Student performance analytics

---

## 👩‍💻 Team Members

* Sowmiya N
* Sivasangeetha D
* Deepika Singh O
* Priyanka D
* Thejashree R

---

## 📜 Conclusion

The AI Math Tutor project demonstrates the power of Generative AI in education by providing an intelligent, interactive, and user-friendly system for solving algebra problems. It enhances conceptual understanding, reduces common mistakes, and supports self-paced learning, making it a valuable tool for modern students.

---

## ⭐ Acknowledgment

This project was developed as part of the **Naan Mudhalvan initiative**, showcasing innovation in AI-based learning systems.

---

## 📌 License

This project is for educational purposes.

---
