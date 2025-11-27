def prime_number_generator(n):
    prime_list = []
    for i in range(2, n + 1):
        is_Prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_Prime = False
                break
        if is_Prime:
            prime_list.append(i)
    return prime_list


print(f"Prime numbers till range are {prime_number_generator(20)}")
