file_name = "lorum_ipsum.txt"
line_count = 0
word_count = 0
char_count = 0
with open(file_name, "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print(f"Line count is: {line_count}")
print(f"Word count is: {word_count}")
print(f"char_count is: {char_count}")
