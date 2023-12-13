import random

print("Guess the number!")

# Generate random number between 1 and 100
secret_num = random.randint(1, 100)

guesses = 0

while True:
    guess = int(input("Enter a guess: "))
    guesses += 1

    if guess == secret_num:
        print("You got it! The number was", secret_num)
        break
    elif guess < secret_num:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

print("You got it in", guesses, "guesses")
