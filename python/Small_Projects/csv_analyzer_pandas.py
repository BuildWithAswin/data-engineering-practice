import pandas as pd


def analyze_csv(filename):
    df = pd.read_csv(filename, encoding="utf-8")

    print(f"Basic info:\n")
    print(df.info())

    print(f"First 5 rows:\n")
    print(df.head())

    print(f"Descriptive statistics:\n")
    print(df.describe())

    print("Unique values per text column:\n")
    for col in df.select_dtypes(include=["object"]).columns:
        unique_count = df[col].nunique(dropna=True)
        print(f" - {col}: {unique_count} unique values")

    print("Missing values in by Column:\n")
    print(df.isnull().sum())

    if "Region" in df.columns and "Quantity" in df.columns:
        print("Total quantity by region:\n")
        print(df.groupby("Region")["Quantity"].sum())


filename = input(f"Enter filename: ").strip()
analyze_csv(filename)
