import pandas as pd
df = pd.read_csv("extract_data.csv")
df.columns = df.columns.str.strip()
print(df.head()) #display first five rows
