# Import modules
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Print logo
print(logo)

# Create a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Starting number of lives and empty list to record guessed letters
guesses = []
lives = 6

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display += "_"
print()

# Use a while loop to let the user guess again while the game has not ended (either word guesses or no lives left)
end_of_game = False
while not end_of_game:

    # TODO-2: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    # For an incorrect guess decrement the lives
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("\nYou have already guessed this letter. Try again.\n")

    else:
        guesses += guess
        position = 0
        for letter in chosen_word:
            if guess == letter:
                display[position] = guess
            position += 1
        print(display)
        if guess not in chosen_word:
            lives -= 1
        print(stages[lives])
        if "_" not in display or lives == 0:
            end_of_game = True

# TODO-3: - If word is guess, print "Congratulations"... else print "You lose"
if lives == 0:
    print("You Lose. The word was " + chosen_word)
else:
    print("Congratulations! You guessed the word!")
