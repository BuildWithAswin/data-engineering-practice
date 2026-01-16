# Using reverse method
# def reverse_string(str):
#    for char in reversed(str):
#        print(char)


# Using slice method
# text = "Hello"
# reverse_string = text[::-1]
# print(reverse_string)

# Using loop
# text = "Hello"
# result = ""
# for ch in text:
#    result = ch + result
# print(result)


# Using recursion
# def reverse_str(str1):
#    if len(str1) == 1:
#        return str1
#    else:
#        return reverse_str(str1[1:]) + str1[0]
#
#
# print(reverse_str("Hello"))

# Using two pointer approach ß

def reverse_string(text):
    chars = list(text)
    l = 0
    r = len(chars) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l = l + 1
        r = r - 1
    return "".join(chars)


print(reverse_string('Hello'))
