def menu_driven_cal():

    task = int(input("Enter 1 for addition\n"
                     "Enter 2 for subtraction\n"
                     "Enter 3 for multiplication\n"
                     "Enter 4 for division\n"
                     "Enter 5 to exit\n"
                     "Your choice: "))
    if task == 1:
        first_digit = int(input("Enter first digit: "))
        second_digit = int(input("Enter second digit: "))
        result = first_digit + second_digit
        print(result)
    elif task == 2:
        first_digit = int(input("Enter first digit: "))
        second_digit = int(input("Enter second digit: "))
        result = first_digit - second_digit
        print(result)
    elif task == 3:
        first_digit = int(input("Enter first digit: "))
        second_digit = int(input("Enter second digit: "))
        result = first_digit * second_digit
        print(result)
    elif task == 4:
        first_digit = int(input("Enter first digit: "))
        second_digit = int(input("Enter second digit: "))
        result = first_digit / second_digit
        print(result)
    elif task == 5:
        print("Exiting..")
        return


menu_driven_cal()
