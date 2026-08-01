print("welcome to game bar") 
print("to guess a number btw 1 to 10")
def guess_number():
    import random
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

guess_number()