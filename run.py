import random
from words import words
import string
from visual import hangman_visual

"""
Ask for users name
Validates the name
"""
name = input('What is your name?').upper()
while not name.isalpha():
    print('invalid name')
    name = input('What is your name?').upper()
    print('Hi', name, 'Lets play Hangman!')

done = False

"""
Gets a random word from the words.py file
"""


def get_word(words):
    """
    Random choice for word from list
    """
    word = random.choice(words)
    return word.upper()

    print(word)
    print('\n')


def hangman():
    """
    Followed tutorial by Kylie Ying (https://www.youtube.com/watch?v=cJJTnI22IF8&list=PLqoebFJFAtg940mqPamWw4_ndWbnfqFqh&index=1&t=3s)
    Letters in the word
    Letters user has guessed
    Getting user input
    Validates for letters only
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


"""
Asks if user wants to replay
or quit the game
"""


while not done:
    hangman()
    again = str(input('Do you want to play again? (type yes or no): '))
    if again == 'no' or 'NO':
        done = True