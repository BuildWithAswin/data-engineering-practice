text_to_write = "I am doing python , python is amazing"
with open("example.txt", "w") as file:
    file.write(text_to_write)
with open("example.txt", "r") as file:
    read_text = file.read()

print("Text from file: ",  read_text)
