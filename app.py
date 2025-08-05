import streamlit as st
import pandas as pd
import numpy as np
import pickle

try:
    with open("linear_regressor_model.pkl", "rb") as file:
        regressor = pickle.load(file)
    with open("column_transformer.pkl", "rb") as file:
        ct = pickle.load(file)
except FileNotFoundError:
    st.error("File Not Found")
    st.stop()

st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("👨‍🎓 Student Performance Predictor")
st.markdown("Enter the student's details below to predict their performance score!")

st.header("Student Information")

previous_score = st.slider("Previous Exam Score", 0 , 100, 0)
extra_acts = ['Yes', 'No']
selected_option = st.selectbox("Have you enrolled for any Extracurricular activities?", extra_acts)
sleep_hrs = st.slider("Daily Avg Sleep", 0 , 12, 7)
sleep_deviation = 1 - (abs(sleep_hrs - 7) / 7)
hours_studied = st.slider("Hours Studied Daily", 0 , 24 - sleep_hrs, 4)
sample_papers = st.slider("Number of Sample Papers Practiced", 0 , 20, 5)

if st.button("Predict Score"):

    user_data = pd.DataFrame([[hours_studied,previous_score,selected_option,sleep_deviation,sample_papers]], 
                             columns=['Hours Studied','Previous Scores','Extracurricular Activities', 'Sleep Deviation',
                                      'Sample Question Pappers Practiced'])
    
    user_data_np = np.array(ct.transform(user_data))

    predicted_score = regressor.predict(user_data_np)
    predicted_score = predicted_score[0] + 20
    if predicted_score >= 100:
        st.success(f"**Predicted Student Performance Score:** 100 out of 100")
    else:
        st.success(f"**Predicted Student Performance Score:** {predicted_score:.2f} out of 100")