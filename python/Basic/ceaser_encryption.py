def ceaser_encrypt(message, k):
    result = ""
    k = k % 26
    for char in message:
        if char.isupper():
            base = ord('A')
            pos = ord(char) - base
            new_pos = (pos + k) % 26
            result += chr(new_pos + base)
        elif char.islower():
            base = ord('a')
            pos = ord(char) - base
            new_pos = (pos + k) % 26
            result += chr(new_pos + base)
        else:
            result += char
    return result


# decrypt function


def ceaser_decrypt(message, k):
    return ceaser_encrypt(message, -k)


message = "Success is the key"
k = 3
encrypted = ceaser_encrypt(message, k)
print(encrypted)
