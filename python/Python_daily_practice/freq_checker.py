# check frequency of a word in an array

def freq_checker(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq


arr = [1, 2, 3, 4, 2, 5, 2, 4]
print(freq_checker(arr))
