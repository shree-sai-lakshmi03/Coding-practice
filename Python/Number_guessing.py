import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess the number.")
print("Good luck!")
n=random.randint(1,100)
for k in range(10):
    guess=int(input("Enter your guess: "))
    if guess>n:
        print("Too high! try again")
    elif guess<n:
        print("Too low! Try again")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
else:
    print("Sorry, you've used all your attempts. The number was", n)
