"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!! ")
    print("You're really good at this! ")

else:
    print("Sorry, you suck at guessing :P ")
    if guess > SECRET:
        print("You guessed too high.")

    else:
        print("You guessed too low.")    
    print("Try again.")    

print("Game over.")