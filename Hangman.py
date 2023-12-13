import random

# List of words to choose from
words = ["python", "programming", "hangman", "games"]

# Pick a random word
word = random.choice(words)

# Create underscores for each letter
blanks = ["_"] * len(word)

# List for incorrect guesses
incorrect = []

# Number of turns
turns = 10

while turns > 0:

    # Show blanks and incorrect guesses
    print(" ".join(blanks))
    print("Incorrect guesses:", end=" ")
    print(", ".join(incorrect))

    # Get player's guess
    guess = input("Guess a letter: ")

    # Check if letter is in word
    if guess in word:
        # Replace blanks with correctly guessed letters
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        # Add guess to incorrect list
        incorrect.append(guess)
        # Decrement turns
        turns -= 1

    # Check if player has won
    if "_" not in blanks:
        print("You won!")
        break

    # Check if player has lost
    if turns == 0:
        print("You lost. The word was:", word)

    # After showing blanks and incorrect guesses

