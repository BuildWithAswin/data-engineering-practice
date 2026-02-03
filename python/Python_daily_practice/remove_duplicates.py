def dup_remove(arr):
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


arr = [1, 1, 2, 3, 4, 4, 5, 5]
print(dup_remove(arr))
