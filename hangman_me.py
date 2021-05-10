import random
from hangman_art import stages, logo
from hangman_words import word_list


# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
len_of_list = len(word_list) - 1
ran_index = random.randint(0, len_of_list)
chosen_word = word_list[ran_index]

# Create a variable and set it to false, the var tracks if it the end of the game.
end_of_game = False

# Create a variable to keep track of the Amount of lives the user has left, start at 6
lives = 6

# Display the HangMan Logo
print(logo)

# Store the length of the chosen word in a variable to re-use it
len_of_chosen_word = len(chosen_word)

# Create an empty List called display. That has enough indexes for the characters in the chosen word, represent those
# characters with '_'
display = []
for index in range(len_of_chosen_word):
    display.append('_')

# Use a while loop to continue looping through the game until the end of the game is reached i.e a user is out of lives
# or has won.
while not end_of_game:
    # Get The Users Guess and store it in a variable in lowercase.
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You\'ve already guessed {guess}')

    # Generate a range of numbers matching the amount of characters in the chosen word. Loop through each character in
    # the chosen word to check if the users guess matches any of the characters in it.
    for index in range(len_of_chosen_word):

        # Set the variable letter to be equal to whatever letter(character) is in currently in the index of the chosen
        # word through each iteration of the loop.
        letter = chosen_word[index]

        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        # If the users guess matches a character in the chosen word, add that character(letter) to the list at the index
        # position it matches the word.
        if letter == guess:
            display[index] = letter

    # Display the characters(letters) that has been guessed correctly.
    # print(display)

    # If the user guessed a letter(character) that is not in the chosen word, after the loop has checked each character
    # decrease their lives by 1
    if guess not in chosen_word:

        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')
        lives -= 1

        # Check if the users don't have any more life and end the game, and Display that they lost.
        if lives == 0:
            end_of_game = True
            print("Game Over.\nYou Lose.")

    # Join all the elements in the list and turn it into a String and Display it.
    print(f"{' '.join(display)}")

    # Check if the list still has any character that has not been guessed correctly, if there is continue the game, if
    # not update the end_of_game variable to True and Display You Win to break out of the While loop.
    if '_' not in display:
        end_of_game = True
        print("Congratulations\nYou win.")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
