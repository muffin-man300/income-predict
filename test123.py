import pandas as pd

df = pd.read_csv("census-income.csv")
df = df.drop(" workclass", axis=1)
df = df.drop(" education", axis=1)
df = df.drop(" marital-status", axis=1)
df = df.drop(" occupation", axis=1)
df = df.drop(" relationship", axis=1)
df = df.drop(" race", axis=1)
df = df.drop(" sex", axis=1)
df = df.drop(" native-country", axis=1)
df = df.dropna()
df[" "] = df[" "].map({" <=50K":0, " >50K":1}).astype(int)

print(df.corr())