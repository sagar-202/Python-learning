import random
word_list = ["banana","apple","mango","pineapple"]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("You win")