def count_occurance(num_list, number):
    count = 0
    for x in range(len(num_list)):
        if num_list[x] == number:
            count += 1
    return count


print(count_occurance([1, 2, 3, 1, 4, 1, 5, 6], 3))
