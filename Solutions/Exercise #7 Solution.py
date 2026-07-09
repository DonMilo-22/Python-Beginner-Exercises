secretNumber = 67
guess = int()

while True:
    guess = int(input("Guess the number: "))

    if guess < secretNumber:
        print("Too low.")
    elif guess > secretNumber:
        print("Too high.")
    else:
        print("Correct!")
        break 
