import pandas as pd
df = pd.read_csv("employees.csv")
filtered = df[df["salary"] > 50000]
filtered.to_csv("high_salary.csv", index=False)
