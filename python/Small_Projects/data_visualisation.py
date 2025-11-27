import pandas as pd
import matplotlib.pyplot as plt


def visualise_data(filename):
    df = pd.read_csv(filename)

    # sanity check
    print("Data preview:\n")
    print(df.head(), "\n")

    if "Region" not in df.columns or "Quantity" not in df.columns:
        print("Required columns not present in file")
        return
    region_summary = df.groupby(
        "Region")["Quantity"].sum().sort_values(ascending=False)
    print(f"Grouped_data:\n", region_summary, "\n")

    # bar chart
    plt.figure(figsize=(8, 5))
    region_summary.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("📊 Total Quantity by Region", fontsize=14)
    plt.xlabel("Region")
    plt.ylabel("Quantity")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


filename = input("Enter filename: ")
visualise_data(filename)
