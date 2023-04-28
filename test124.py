"""
import numpy as np
from sklearn import linear_model
import pandas as pd

 
edu_n = int(input("Enter num of years - "))

df = pd.read_csv("census-income.csv")

X = np.array(df[" education-num"]).reshape(-1, 1)
y = np.array(df[" "].map({" <=50K":1, " >50K":0}))

logr = linear_model.LogisticRegression()
logr.fit(X,y)

prediction = logr.predict(np.array([edu_n]).reshape(-1, 1))
print(prediction)


if prediction == np.array([0]):
    print("Income greater than $50K")
else:
    print("Income less or equal to $50K")

"""


import pandas
from sklearn import linear_model

df = pandas.read_csv("census-income.csv")


edu_num = abs(int(input("Enter number of years of education - ")))
hours_per_week = abs(int(input("Enter number of hours per week - ")))

x = df[[" education-num", " hours-per-week"]]
y = df[" "].map({' <=50K':1,' >50K':0})



lin_reg = linear_model.LinearRegression()
lin_reg.fit(x.values, y)

pred = lin_reg.predict([[edu_num, hours_per_week]])


print("1: <=$50K \n0: >$50K")


f_prediction = round(float(pred[0]))

if f_prediction == 1 or f_prediction == 0:
    print("OUTPUT: ",round(float(pred[0])))      # OUTPUT IS NOT EXACT BUT GIVES A GENERAL IDEA
    print("EXACT PREDICTED VALUE BY MODEL: ",float(pred[0]))
else:
    print("There was an error in calculation, please input valid values.")
    print("EXACT PREDICTED VALUE BY MODEL: ",float(pred[0]), "(Likely greater than $50K)")




