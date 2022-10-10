# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string
from visual import hangman_visual

name = input('Player name?').upper()
print('Hi', name, 'Lets play Hangman!')


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
    score = 0

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(name,',you have', lives, 'lives left. Letters already used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual[lives])
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('It is not there,',name,'try again')

        elif user_letter in used_letters:
            print('You already used. Try again')
        
        else:
            print('invalid choice. Try again')

    if lives == 0:
        print('No more lives. The word was', word, '!!!')
        print('Your score is',score)
    else:
        score = + 1
        print('You got it!')
        print('Your score is',score)


hangman()


again = str(input("Do you want to play again (type yes or no): "))
if again == "yes":
    hangman()
else:
    name