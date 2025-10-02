import random
word_list = ["banana","apple","mango","pineapple"]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")