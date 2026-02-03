def min_max_checker(arr):
    min = arr[0]
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max


arr = [1, 2, 3, 4]
print(min_max_checker(arr))
