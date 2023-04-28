import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

edun = int(input("Enter num edu - "))
hpw = int(input("Enter hours - "))

df = pd.read_csv("census-income.csv")

X = np.array(df[" education-num"]).reshape(-1, 1)
y = np.array(df[" hours-per-week"]).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

y_pred = lin_model.predict(np.array([edun, hpw]).reshape(-1, 1))

print(y_pred)