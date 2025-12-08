
import csv
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i < 5:
            print(row)
