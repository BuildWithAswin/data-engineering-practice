def largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest


print(largest([1, 2, 3, 4]))
