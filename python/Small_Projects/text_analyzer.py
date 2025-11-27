vowels = ["a", "e", "i", "o", "u"]
consonents = consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']



def check_vowels():
    with open("sample.txt", "r") as file:
        vowels_count = 0
        for line in file:
           for vow in line.lower():
               if vow in vowels:
                vowels_count += 1
    print (f"Number of vowels is : {vowels_count}")  
   
def check_consonents():
       with open("sample.txt", "r") as file:
        consonents_count = 0 
        for line in file:
           for cons in line.lower():
               if cons in consonents:
                consonents_count += 1
       print (f"Number of consonents is : {consonents_count}")

def longest_word():
      list_words = []
      with open("sample.txt", "r") as file:
       for line in file:
          words = line.split()
          for word in words:
             list_words.append(word)
      longest = max(list_words, key=len)
      print (f"Longest word: {longest}")      

check_vowels()
check_consonents()
longest_word()







