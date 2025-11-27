def bubble_sort(numbers):
    n = len(numbers)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break


numbers = [65, 47, 12, 26, 87, 34, 96]
print(f"Before sorting:   {numbers}")

bubble_sort(numbers)

print(f"After sorting:  {numbers}")
