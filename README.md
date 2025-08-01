# 📚 Student Performance Predictor — Linear Regression with Categorical Data

This is a beginner-level machine learning project where I used **Linear Regression** to predict student scores based on features like hours studied, attendance, and subject.

I also worked with **categorical data** (e.g., Subject names), which I encoded using OneHotEncoder to train the model properly.

---

## 📁 What’s Inside

- `Student_Performance.csv`: The dataset  
- Python script that:
  - Loads and explores the data using Pandas
  - Preprocesses categorical features using **OneHotEncoding**
  - Splits data into training and test sets
  - Trains a **Linear Regression** model
  - Compares predicted vs actual values
  - Visualises the result using **Seaborn**

---

## 🛠 Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- scikit-learn

---

## 🎯 Model Accuracy

- **R² Score**: Gives a good idea of how well the model fits
- Visual inspection with an **Actual vs Predicted** scatterplot  
  _(Ideal results form a diagonal line)_

---

## 🧪 What I Learned

- Handling **categorical variables** with OneHotEncoding
- How the train-test split works
- Model evaluation using `r2_score`
- Visualising predictions to catch errors better

---

## 🚀 Run it Yourself

```bash
# Clone the repo
git clone https://github.com/YashDahiwlikar914/Student-Performance-Predictor.git

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run the script
python Main.py
