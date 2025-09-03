# CarrerMentor AI- an AI powered Carrer Recommendation System

## Problem Statement
Choosing the right career path is a critical decision for students and professionals, but it is often overwhelming.
Many individuals struggle to:

1]Understand which careers match their unique skills and educational background.

2]Identify the learning paths, courses, and projects that will prepare them for those careers.

3]Access personalized guidance without spending thousands on career counseling.

4]The lack of personalized, accessible, and AI-driven guidance results in confusion, wasted time, and missed opportunities.

## Solution Proposed
CareerMentor AI is an AI-powered career guidance platform designed to solve this problem by:

1]Analyzing user profiles (skills, education, interests).

2]Recommending top career matches with match percentages and descriptions.

3]Providing learning pathways — courses, projects, and roadmaps to help users upskill.

4]Accessible via the web (Flask app deployed on cloud platforms like Render or AWS).

5]Built with Python, Flask, and AI models for recommendations — ensuring fast, intelligent, and user-friendly interaction.

## Features
- 🧠 **AI-powered Career Recommendations** — Get top career options based on skills and education.
- 🛤 **Career Pathways** — View recommended courses, roadmaps, and projects for each career.
- 🎨 **Modern UI** — Clean, responsive interface built with Bootstrap 5.
- 🖥 **Web-based & Lightweight** — Runs on Flask, easy to deploy locally or on cloud (Render).
- 🔗 **Extensible** — Can integrate with AI models like Google Gemini or custom ML models for smarter recommendations.
- 🐳 **Docker Support** — Easily containerize and deploy anywhere.


##  Demo

Try it:https://carrermentor-ai-1.onrender.com/

## Tech Stack Used
-Python
-Flask
-HTML
-CSS
-Bootstrap
-Jinja2
-Gunicorn
-Render (for deployment)
-Docker (optional, for containerization)

## How to Run
**Step 1. Clone the repository.**
```powershell
git clone https://github.com/harshvgangawane/customer-churn-prediction-system.git
cd "Customer Churn Prediction"
```
**Step 2. (Optional) Create a virtual environment.**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
**Step 3. Install the requirements**
```powershell
pip install -r requirements.txt
```
**Step 4. Run the Streamlit app**
```powershell
python run app.py
```

## Project Architecture
src/ – Core logic (career recommendation & pathway generation)

templates/ – HTML templates (home.html, carrer_recommendations.html, pathways.html)

static/ – Static assets (CSS, JS, images)

app.py – Main Flask application

requirements.txt – Dependencies

Dockerfile – (Optional) Containerization support


## Notebooks

This project does not rely on Jupyter notebooks as it is primarily a web-based recommendation platform.

## Models Used
Currently, the system uses prompt-based AI recommendations.
Optionally, you can integrate:

LLMs like Google Gemini (Generative AI)



## Conclusion
CareerMentor AI provides an interactive and AI-assisted way for individuals to explore career options aligned with their skills and education. It serves as a foundation that can be extended with data-driven models, real-time labor market data, or advanced personalization for better career guidance.
