import string


def password_checker(input_string):
    has_upper = False
    has_lower = False
    has_numer = False
    has_special = False

    for char in input_string:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in string.punctuation:
            has_special = True

    if has_lower and has_number and has_upper and has_special:
        return "Strong password"
    else:
        return "Weak password"


print(password_checker("Pass4123"))
