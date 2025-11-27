def count_words(sentense, word):
    count = 0
    word_list = sentense.split()
    for w in word_list:
        if w == word:
            count += 1
    return count


print(count_words("I am doing python , python is amazing", "python"))
