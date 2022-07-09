"""One shot wordle program!"""

__author__ = "730462090"

secret_word: str = "python"
len_of_word: int = len(secret_word)

# Asking user for input and saving their guess in the user_guess variable
user_guess: str = input(f"What is your {len_of_word}-letter guess? ")
while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len_of_word} letters! Try again: ")

# Variable definitions in order to check for matching letters and string them together.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_tracker: int = 0
color_boxes: str = ""
character_exists: bool = False


while index_tracker < len(secret_word):
    # If letter and positions match, will output a green box
    if user_guess[index_tracker] == secret_word[index_tracker]:
        color_boxes = color_boxes + GREEN_BOX
    else:
        alternate_check: int = 0
        character_exists = False
        # Loop will check for matching alternate indices and if they match, it will set the condition of variable
        # to true (indicating a yellow box will need to be added), if they do not match it will run through all the alternate indices
        # of the secret word (until the length of the word is completed) to see if a match exists.
        # If it runs through the length of the secret word with no match, boolean variable will still be false which will then print a white box.
        while character_exists is not True and alternate_check < len(secret_word):
            if secret_word[alternate_check] == user_guess[index_tracker]:
                character_exists = True
            else:
                alternate_check = alternate_check + 1
        if character_exists is True:
            color_boxes = color_boxes + YELLOW_BOX
        if character_exists is False:
            color_boxes = color_boxes + WHITE_BOX
    index_tracker = index_tracker + 1

print(color_boxes)

# Printing of the final message if user guess exactly matches secret word or not
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")