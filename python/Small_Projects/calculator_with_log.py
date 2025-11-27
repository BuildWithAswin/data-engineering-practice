import os
from datetime import datetime
current_time = datetime.now()

filename = "calculator.log"
def logging(first_digit, second_digit, operator, result):
        current_time = datetime.now()
        with open (filename, "a") as f:
                f.write(f"{current_time}: {first_digit} {operator} {second_digit} = {result}\n")

operation = int(input("Enter 1 for addition: " \
                   "Enter 2 for subtraction: " \
                   "Enter 3 for multiplication: " \
                   "Enter 4 for division: "))



if operation == 1:
     first_digit = int(input("Enter the first digit: "))
     second_digit = int(input("Enter the second digit: "))
     operator = "+"
     result = first_digit + second_digit
     print (f"{first_digit} {operator} {second_digit} = {result}")
elif operation == 2:
     first_digit = int(input("Enter the first digit: "))
     second_digit = int(input("Enter the second digit: "))
     operator = "-"
     result = first_digit - second_digit
     print (f"{first_digit} {operator} {second_digit} = {result}")
    
elif operation == 3:
     first_digit = int(input("Enter the first digit: "))
     second_digit = int(input("Enter the second digit: "))
     operator = "*"
     result = first_digit * second_digit
     print (f"{first_digit} {operator} {second_digit} = {result}")

else: 
    first_digit = int(input("Enter the first digit: "))
    second_digit = int(input("Enter the second digit: "))
    operator = "/"
    result = first_digit / second_digit
    print (f"{first_digit} {operator} {second_digit} = {result}")

logging(first_digit, second_digit, operator, result)
print(f"Logged to {filename}")



