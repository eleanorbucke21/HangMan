import asyncio
import websockets
import random
import string
from words import words
from visual import hangman_visual

"""
Adapts the existing hangman() function for WebSocket-based communication.
"""

def get_word(words):
    """
    Randomly selects a word from the list of words.
    """
    return random.choice(words).upper()

"""
Followed tutorial by Kylie Ying (https://www.youtube.com/watch?v=cJJTnI22IF8&list=PLqoebFJFAtg940mqPamWw4_ndWbnfqFqh&index=1&t=3s)
Letters in the word
Letters user has guessed
Getting user input
Validates for letters only
 """

async def hangman(websocket, name):
    """
    Adapts the original hangman() function for WebSocket communication.
    Handles game logic using WebSocket to send and receive messages.
    """
    word = get_word(words)
    word_letters = set(word)  # Letters in the word to guess
    alphabet = set(string.ascii_uppercase)  # All possible valid letters
    used_letters = set()  # Letters guessed by the user
    allowed_errors = 6  # Number of lives

    # Main game loop
    while allowed_errors > 0 and len(word_letters) > 0:
        # Send game state to the client
        await websocket.send(f"{name}, you have {allowed_errors} lives left. Letters already used: {', '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        await websocket.send(hangman_visual[allowed_errors])
        await websocket.send(f"Current word: {' '.join(word_list)}")

        # Get the user's guess
        await websocket.send("Guess a letter:")
        user_letter = await websocket.recv().upper()

        # Validate the guess
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correct guess
                await websocket.send(f"Good job! {user_letter} is in the word.")
            else:
                allowed_errors -= 1  # Incorrect guess
                await websocket.send(f"Oops! {user_letter} is not in the word. Try again.")
        elif user_letter in used_letters:
            await websocket.send("You already guessed that letter. Try a different one.")
        else:
            await websocket.send("Invalid input. Please guess a letter.")

    # End of the game
    if len(word_letters) == 0:
        await websocket.send(f"Congratulations, {name}! You guessed the word: {word}.")
    else:
        await websocket.send(f"Game over, {name}. The word was: {word}.")

async def main(websocket, path):
    """
    Handles the WebSocket connection and runs the adapted Hangman game.
    """
    await websocket.send("Welcome to Hangman!")
    await websocket.send("What is your name?")

    # Get player's name
    name = await websocket.recv()
    while not name.isalpha():
        await websocket.send("Invalid name. Please enter letters only.")
        name = await websocket.recv()

    await websocket.send(f"Hi {name}, let's play Hangman!")
    await hangman(websocket, name)

# Start the WebSocket server
start_server = websockets.serve(main, "0.0.0.0", 8000)

if __name__ == "__main__":
    """
    Runs the WebSocket server.
    """
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
