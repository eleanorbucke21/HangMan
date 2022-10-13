# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string
from visual import hangman_visual

name = input("What is your name?").lower()
while not name.isalpha():
    print("invalid name")
    name = input("What is your name?").lower()
    print('Hi', name, 'Lets play Hangman!')

done = False


def get_word(words):
    """
    random choice for word from list
    """
    word = random.choice(words)
    return word.upper()

    print(word)
    print('\n')


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

    allowed_errors = 6

    while allowed_errors > 0 and len(word_letters) > 0:
        print(name, ',you have', allowed_errors, 'lives left. Letters already used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual[allowed_errors])
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                allowed_errors = allowed_errors - 1
                print('It is not there,', name, 'try again')

        elif user_letter in used_letters:
            print('You already used. Try again')
        else:
            print('invalid choice. Try again')

        if allowed_errors == 0:
            print('No more lives. The word was', word, '!!!')
            break

        if len(word_letters) == 0:
            print('You got it!')
            word = get_word(words)
            word_letters = set(word)
            used_letters = set()


while not done:
    hangman()
    again = str(input('Do you want to play again? (type yes or no): '))
    if again == 'no':
        done = True