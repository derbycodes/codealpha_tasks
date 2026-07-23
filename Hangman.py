
import random

# ------------------------------------------------------------
# A small predefined list of words to guess from — no file or
# API needed, just a plain Python list of strings.
# ------------------------------------------------------------
WORDS = ["python", "hangman", "keyboard", "science", "gorilla"]

MAX_WRONG_GUESSES = 6


def choose_word(word_list):
    """Pick one random word from the list."""
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    """
    Build the current display of the word, e.g. 'p _ t h _ n'
    showing correctly guessed letters and blanks for the rest.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []      # letters the player has already tried
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word. You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'none yet'}")

        guess = input("\nGuess a letter: ").lower().strip()

        # --- Basic input validation ---
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # --- Check for a win: every letter in the word has been guessed ---
        if all(letter in guessed_letters for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    # --- Player ran out of guesses ---
    print(f"Game over! You ran out of guesses. The word was '{word}'.")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
