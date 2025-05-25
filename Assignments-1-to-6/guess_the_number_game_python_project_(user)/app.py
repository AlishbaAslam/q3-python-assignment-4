import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()