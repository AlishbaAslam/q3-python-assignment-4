import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'computer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)          # letters in the word
    guessed_letters = set()           # letters guessed so far
    tries = 6                        # max tries
    print("Welcome to Hangman!")

    while tries > 0 and len(word_letters) > 0:
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in guessed_letters else '_' for letter in word]))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Tries left: {tries}")

    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word '{word}' correctly!")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()