import random
from art import stages, logo
from hangman_words import word_list
print(logo)
hangman = stages
chosen_word = random.choice(word_list)


display = []
for _ in chosen_word:
    display += "_"
lives = 6

while "_" in display:
    guess = input("Please choose a letter\n").casefold()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        print(hangman[lives])
        if lives == 0:
            print("you lose")
            break
else:
    print("You win")

