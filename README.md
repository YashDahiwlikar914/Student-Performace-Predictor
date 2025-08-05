# Student Performance Predictor — ML + Streamlit App

This project uses a **Linear Regression model** to predict a student’s performance score based on input features like sleep hours, study time, extracurricular activity, etc.  
It’s deployed as a clean, minimal **Streamlit web app**.

The focus was on learning:
- how to work with **categorical + numerical features**
- how to use a **ColumnTransformer**
- how to save and reuse ML models
- and how to deploy everything smoothly using Streamlit

## Live App

👉 [Open the App](https://studentperformacepredictor.streamlit.app/)  

## What It Does

- Takes in 5 student-related inputs:
  - Previous exam score
  - Extracurricular participation (Yes/No)
  - Average sleep hours
  - Daily study hours
  - Number of sample papers practised
- Processes the data (with encoding where needed)
- Uses a trained **Linear Regression model** to predict performance score out of 100
- Shows result in real-time on a simple UI

## Key Concepts Practised

- Encoding categorical features using **OneHotEncoder**
- Keeping input format consistent using **ColumnTransformer**
- Saving both model & transformer using **`pickle`**
- Deploying with a clean interface using **Streamlit**
- Error handling in deployed app (for missing files, etc.)

## How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com//YashDahiwlikar914/Student-Performace-Predictor.git
cd Student-Performace-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model (if not already)

```bash
python train_model.py
```

### This script will:
- Encode categorical features using OneHotEncoder
- Train a LinearRegression model
- Save both the model (linear_regressor_model.pkl) and transformer (column_transformer.pkl) for use in the app

### 4. Launch the Streamlit app

```bash
streamlit run app.py
```
The app will open in your browser at http://localhost:8501


## requirements.txt
```txt
streamlit
scikit-learn
pandas
numpy
```

This is needed for local setup and deployment on Streamlit Cloud. Without it, the app will throw ModuleNotFoundError.

## How the Code Works
#### train_model.py
- Loads the CSV dataset
- Encodes the Extracurricular Activities column using OneHotEncoder
- Fits a LinearRegression model
- Saves both the model and encoder using pickle

#### app.py
- Loads the model and transformer at the start
- Collects user input via Streamlit UI (sliders and dropdown)
- Converts input into a DataFrame
- Transforms it using the saved encoder (column_transformer.pkl)
- Passes it to the model for prediction
- Displays the predicted score
- The app also checks if the saved model files are missing — instead of crashing, it shows a clean error message so you know what's wrong.

## Model Input/Output Details
- Input Columns:
  - Hours Studied (numeric)
  - Previous Score (numeric)
  - Extracurricular Activities (categorical → encoded)
  - Sleep Hours (numeric)
  - Sample Papers Practised (numeric)
- Output:
  - Predicted Performance Score (0 to 100)

