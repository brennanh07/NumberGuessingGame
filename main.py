import random

# Determines total amount of guesses allowed based on game difficulty selected


def guesses_allowed(game_difficulty):
    if game_difficulty == "easy":
        return 10
    elif game_difficulty == "hard":
        return 5


def display_guesses(guesses_left):
    print(f"You have {guesses_left} guesses left.")


# End game if user has no guesses left
def life_check(guesses_left, number):
    if guesses_left == 0:
        print(f"You ran out of guesses. The number was {number}.")
        return False
    else:
        return True


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

# Generate random number
random_num = random.randint(1, 100)

# Takes user game difficulty input. If not a valid input, asks for input again.
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        break

num_guesses = guesses_allowed(difficulty)

display_guesses(num_guesses)

play_game = True

while play_game:
    # Only accept user input if it's an integer and doesn't produce a value error
    while True:
        try:
            if num_guesses == 1:
                user_guess = int(input("Last guess!: "))
            else:
                user_guess = int(input("Make a guess: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    # If guess is too high or low, gives feedback and reduces guesses left by 1
    if user_guess > random_num:
        print("Too high. Guess again.")
        num_guesses -= 1
        display_guesses(num_guesses)
    elif user_guess < random_num:
        print("Too low. Guess again.")
        num_guesses -= 1
        display_guesses(num_guesses)

    # Check if user still has > 0 guesses left
    play_game = life_check(num_guesses, random_num)

    # Check if user guessed number correctly
    if user_guess == random_num:
        print(f"You got it! The number was {random_num}.")
        play_game = False
