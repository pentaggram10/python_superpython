import random

# Generate a random 3-digit number
answer = str(random.randint(100, 999))

while True:
    # Get user's guess
    guess = input("Guess a 3-digit number: ")

    # Check if guess is valid
    if not guess.isdigit() or len(guess) != 3:
        print("Invalid input. Please enter a 3-digit number.")
        continue

    # Check for correct digits in the right place
    strikes = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strikes += 1

    # Check for correct digits in the wrong place
    balls = 0
    for i in range(3):
        if guess[i] in answer and guess[i] != answer[i]:
            balls += 1

    # Print results
    if strikes == 3:
        print("You win!")
        break
    else:
        print("{} strikes, {} balls".format(strikes, balls))
