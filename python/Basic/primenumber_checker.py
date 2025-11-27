def primenumber_checker(num):
    if num <= 1:
        print("number is not prime")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            return
    print(f"{num} is a prime number")


primenumber_checker(29)
