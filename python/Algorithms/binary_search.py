def binary_search(arr, target):
    low = arr[0]
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            arr[high] = mid - 1
    return -1  # not found


arr = [1, 2, 3, 4, 5, 6]
target = 10
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
