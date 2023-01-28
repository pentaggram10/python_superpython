import random

# List of words to choose from
words = ["kimyonggyu"]

# Choose a random word
answer = random.choice(words)

# Create a list of underscores the same length as the answer
display = ["_"] * len(answer)

# Number of allowed incorrect guesses
guesses_allowed = 50000000000000000000000000000000000

# Number of incorrect guesses so far
guesses_made = 0

# Keep track of letters already guessed
guessed_letters = set()

while guesses_made < guesses_allowed:
    # Get user's guess
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # Add the letter to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the letter is in the answer
    if guess in answer:
        # Replace underscores with the correctly guessed letter
        for i in range(len(answer)):
            if answer[i] == guess:
                display[i] = guess
        print(" ".join(display))

        # Check if the player has won
        if "_" not in display:
            print("You win!")
            break
    else:
        guesses_made += 1
        print("Incorrect. You have {} guesses left.".format(guesses_allowed - guesses_made))

if guesses_made == guesses_allowed:
    print("You lose! The word was {}.".format(answer))
