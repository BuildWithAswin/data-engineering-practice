def sum_of_list(num):
    sum = 0
    for x in range(len(num)):
        sum += num[x]
    return sum


print(sum_of_list([1, 2, 3, 4]))
