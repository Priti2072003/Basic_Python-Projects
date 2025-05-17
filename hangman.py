import random

 # Hangman Game
def choose_word():
    """Selects a random word from a predefined list."""
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    """Displays the current state of the word with guessed letters revealed."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_game():
    """Runs the Hangman game."""
    secret_word = choose_word()
    word_length = len(secret_word)
    guessed_letters = set()
    attempts_left = 6  # You can adjust the number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print(f"The secret word has {word_length} letters.")
    print(display_word(secret_word, guessed_letters))
    print(f"You have {attempts_left} incorrect attempts remaining.")

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
            current_display = display_word(secret_word, guessed_letters)
            print(current_display)
            if "_" not in current_display:
                print("Congratulations! You guessed the word:", secret_word)
                break
        else:
            attempts_left -= 1
            print(f"Incorrect guess. You have {attempts_left} attempts remaining.")
        print(display_word(secret_word, guessed_letters))

        if attempts_left == 0:
            print("You ran out of attempts. The secret word was:", secret_word)

if __name__ == "__main__":
    hangman_game()

print("\n" + "="*30 + "\n")


