def palindormechecker(word):
    word = word.lower()
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    else:
        return True


print(palindormechecker("Madam"))
