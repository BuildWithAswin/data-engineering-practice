import csv
from statistics import mean


def analyze_csv(filename):
    with open(filename, newline='', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

# Basic count
    print(f"Total rows: {len(rows)}")

    prices = [float(row["Price"]) for row in rows]
    quantities = [int(row["Quantity"]) for row in rows]

# stats
    print(f"Average price: {mean(prices):.2f}")
    print(f"Total Quantity: {sum(quantities)}")
    print(f"Highest price: {max(prices)}")
    print(f"Lowest: {min(prices)}")


filename = input(f"Enter the filename: ").strip()
analyze_csv(filename)
