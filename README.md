# My Diabetes Prediction App

Welcome to my personal project! This application uses machine learning to predict the likelihood of diabetes based on clinical and lifestyle data. I built a user-friendly interface with Streamlit, containerized the app with Docker for consistency, and even set up deployment instructions for Azure. This project is a true labor of love, combining my passion for healthcare and technology.

---

## Project Overview

In this project, I trained a machine learning model to predict diabetes. The model considers several features such as:
- **Gender** (encoded as Male=0, Female=1)
- **Age**
- **Hypertension** (0 for No, 1 for Yes)
- **Heart Disease** (0 for No, 1 for Yes)
- **Smoking History** (e.g., Never=0, Former=1, Current=2, Unknown=3)
- **BMI**
- **HbA1c Level**
- **Blood Glucose Level**

By inputting these details into the app, the model returns a prediction indicating whether a patient is diabetic or not.

---

## Running the App Locally

If you'd like to run the app on your own machine, follow these simple steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Install the required dependenies**
   ```bash
   pip install -r requirements.txt

3. **Start the streamlit app** 
      
      ```bash
    streamlit run streamlit_app.py
    Open your browser and go to http://localhost:8501 to interact with the app.


## Docker Deployment 
To ensure the app runs consistently on any machine, I containerized it with Docker.

1. **Build the Docker Image**

   ```bash
   docker build -t diabetes-prediction-app .
   
2. **Run the Docker Container**

   ```bash
   docker run -p 8501:8501 diabetes-prediction-app
   Your app will now be accessible at http://localhost:8501.

## Global Deployment on Streamlit Community Cloud

I’m excited to share that I have deployed this app on Streamlit Community Cloud so that it can be assessed globally! With Streamlit Cloud, the app is hosted publicly, meaning anyone in the world can interact with it via a simple web link.

You can visit the app here: https://share.streamlit.io/your-username/Diabetes_prediction/main/streamlit_app.py