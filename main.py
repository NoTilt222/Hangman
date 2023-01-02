import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
word_length = len(chosen_word)
lives = 6
blank = []
test1 = True

print(logo)
# print(f"The chosen word is {chosen_word}")
for _ in range(word_length):
    blank += "_"

while blank != chosen_word_list:
    if 0 < lives <= 6:
        guess = input("What letter do you want to guess? ").lower()
        if guess in blank:
            print(f"You've already guessed {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                blank[position] = guess
        # test = ""
        # for a in blank:
        # test += a
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lost a life.")
        print(f"{''.join(blank)}")
    elif lives == 0:
        print("You lost")
        print(f'the chosen word was {chosen_word}')
        break
    print(stages[lives])
else:
    print("You won!")
