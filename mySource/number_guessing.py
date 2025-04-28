from random import seed, randint

# Generate a random number between 1 and 10
number = randint(1, 10)

winner = False

# Game Loop (until player guesses)
while winner == False:
    # Ask player for a guess
    guess = int(input("Guess a number between 1 and 10: "))
    
    # If it's correct, change the exit condition
    if guess == number:
        winner = True
        print("You got it!")
    elif guess < number:
        print("Too low!  Try again.")
    elif guess > number:
        print("Too high! Try again.")