user_word = input("enter a word: ")
user_word = user_word.upper()
word=""

for letter in user_word:
    if letter == "A":continue
    elif letter == "E":continue
    elif letter == "I":continue
    elif letter == "O":continue
    elif letter == "U":continue
    else: word += letter
print(word)