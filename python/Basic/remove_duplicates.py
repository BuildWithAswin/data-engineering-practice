def remove_duplicates(num):
    result = []
    for x in range(len(num)):
        duplicates = False
        for y in range(x):
            if num[x] == num[y]:
                duplicates = True
                break
        if not duplicates:
            result.append(num[x])
    return result


print(remove_duplicates([1, 2, 2, 3, 3, 4]))
