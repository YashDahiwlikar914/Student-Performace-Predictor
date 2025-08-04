import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
import pickle
import numpy as np

Data = pd.read_csv("Student_Performance.csv")

x = Data.iloc[:,:-1].values
y = Data.iloc[:,-1].values

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [2])], remainder="passthrough")
x = np.array(ct.fit_transform(x))

regressor = LinearRegression()

regressor.fit(x, y)
with open("linear_regressor_model.pkl", "wb") as f:
    pickle.dump(regressor, f)

with open("column_transformer.pkl", "wb") as f:
    pickle.dump(ct,f)
