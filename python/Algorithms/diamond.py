def diamond(n):
    pattern = ""
    for i in range(0, n):
        pattern += " " * (n - i) + "*" * (2 * i - 1) + "\n"
    for i in range(n, 0, -1):
        pattern += " " * (n - i) + "*" * (2 * i - 1) + "\n"

    return pattern


print(diamond(5))
