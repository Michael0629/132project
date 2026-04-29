import random

def get_difficulty():
    attempts_difficulty = {"easy": 25, "medium": 15, "hard": 10}

    difficulty = input("Choose game difficulty - easy, medium, or hard: ").lower()

    while difficulty not in attempts_difficulty:
        print("You've entered an invalid difficulty. Please enter easy, medium, or hard.")
        print()
        difficulty = input("Choose game difficulty - easy, medium, or hard: ").lower()

    return attempts_difficulty[difficulty]


    

def number_guessing_game():
    num = random.randint(1, 100)

    attempts = 0
    correct_guess = False
    
    print("Hello! Welcome to the Number Guessing Game!")
    print()
    print("There is a number in my head between 1 and 100")
    print()

    max_attempts = get_difficulty()

    
    print()
    print(f"Based on your selected difficulty, you have {max_attempts} attempts to guess the correct number. Good Luck!")
    print()

    while not correct_guess and attempts < max_attempts:
        guess = input("Enter your guess: ")
        
        if guess.isdigit():
            guess = int(guess)
            attempts += 1

            if guess < num:
                print("Too Low! Guess a higher number.")
                print()
            elif guess > num:
                print("Too High! Guess a lower number.")
                print()
            else:
                print()
                print("Correct!")
                print()
                print(f"Congratulations! It took you {attempts} attempts to guess the correct number.")
                correct_guess = True
        else:
            print("The number you entered is invalid. Enter a valid number.")
            print()
    if not correct_guess:
        print(f"Oh no! You ran out of attempts! The number was {num}.")

number_guessing_game()