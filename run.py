# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

print(words)


def get_word(words):
    """
    random choice for word from list
    """
    word = random.choice(words)
    return word.upper()

    print(word)


def hangman():
    """
    letters in the word
    letters user has guessed
    getting user input
    """
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left. Letters already used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('It is not there, try again')

        elif user_letter in used_letters:
            print('You already used. Try again')
        
        else:
            print('invalid choice. Try again')

    if lives == 0:
        print('No more lives. The word was', word, '!!!')
    else:
        print('You got it!')


hangman()

user_input = input('Type something:')
print(user_input)
