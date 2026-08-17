print("welcome to game bar") 
print("to guess a number btw 1 to 100")
def guess_number():
    import random
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        clue = input("Do you want a clue? (yes/no): ").strip().lower()
        if clue == "yes":
            if number_to_guess % 2 == 0:
                print("Clue: The number is even.")
            else:
                print("Clue: The number is odd.")
        if clue == "no":
            print("No clue will be provided. Good luck!")
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