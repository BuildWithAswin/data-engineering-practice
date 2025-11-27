def anagram_checker(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)


print(anagram_checker("listen", "silent"))
