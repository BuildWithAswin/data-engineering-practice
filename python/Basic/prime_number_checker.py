def prime_number_cehck(num):
    if num <= 1:
        print(f"{num} is not a prime number")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
        return

    print(f"{num} is a prime number")


prime_number_cehck(18)
