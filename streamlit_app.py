import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('diabetes_prediction_gb_model1.pkl')

# Streamlit UI
st.title("Diabetes Prediction App")
st.write("Enter patient details to predict diabetes outcome.")

# Gender Selection
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Convert gender to numerical (assuming encoding: Male=0, Female=1, Other=2)
gender_dict = {"Male": 0, "Female": 1, "Other": 2}
gender_encoded = gender_dict[gender]

# Other Inputs
age = st.number_input("Age", min_value=0, max_value=120, step=1)
hypertension = st.radio("Hypertension", [0, 1])
heart_disease = st.radio("Heart Disease", [0, 1])
smoking_history = st.selectbox("Smoking History", ["Never", "Former", "Current", "Unknown"])

# Encode Smoking History (Example encoding)
smoking_dict = {"Never": 0, "Former": 1, "Current": 2, "Unknown": 3}
smoking_encoded = smoking_dict[smoking_history]

bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)
HbA1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, step=0.1)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=400, step=1)

# Prediction button
if st.button("Predict Diabetes"):
    # Prepare input data
    input_data = np.array([gender_encoded, age, hypertension, heart_disease, smoking_encoded, bmi, HbA1c_level, blood_glucose_level]).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    st.success(f"Prediction: {result}")