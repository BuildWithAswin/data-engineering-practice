def linear_search(arr, num):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == num:
            return (f"Element {num} found at index {i}!")
    return ("Element not found in the list")


arr = [1, 2, 3, 4, 5, 6]
print(linear_search(arr, 6))
