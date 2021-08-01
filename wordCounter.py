text = input("Enter your text: ")
words = 1
characters = 0
sentences = 0
for letter in text:
    characters += 1
    if letter == " ":
        words += 1
    elif letter == "!" or letter == "?" or letter == ".":
        sentences += 1
print("Characters: ", characters)
print("Sentences: ", sentences)
print("Words: ", words)
    
