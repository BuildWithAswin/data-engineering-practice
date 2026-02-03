def second_largest(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    second_largest = len[arr] - 1
    return second_largest


arr = [4, 3, 2, 1]
print(second_largest(arr))
