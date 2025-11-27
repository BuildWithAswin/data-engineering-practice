def numbertriangle(rows):
    result = ""
    for row in range(1, rows+1):
        for col in range(1, row+1):
            result += str(col) + " "
        result += "\n"
    return result


print(numbertriangle(5))
