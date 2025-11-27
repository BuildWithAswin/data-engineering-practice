def check_unique_words(sentence):
    word_list = sentence.split()
    result = []
    for w in word_list:
        if w not in result:
            result.append(w)
    return result


print(check_unique_words("I am doing python , python is amazing"))
