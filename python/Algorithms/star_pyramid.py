def star_pyramid(n):
    pattern = ""
    for i in range(1, n + 1):
        pattern += " " * (n - i) + "*" * (2 * i - 1) + "\n"
    return pattern


print(star_pyramid(5))
