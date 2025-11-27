students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Emma": 95,
    "Frank": 78,
    "Grace": 88,
    "Henry": 55,
    "Ivy": 60,
    "Jack": 82
}

# highest
highest = -1
topper = ""
for name, mark in students.items():
    if mark > highest:
        highest = mark
        topper = name
print(f"{topper} has the highest score!: {highest}")

# lowest
lowest = float('inf')
least = ""
for name, mark in students.items():
    if mark < lowest:
        lowest = mark
        least = name
print(f"{least} has the lowest score!: {lowest}")

# average
max_mark = len(students) * 100
total_mark = 0
for student, mark in students.items():
    total_mark += mark
print(f"Average mark is: {total_mark/max_mark * 100} %")
