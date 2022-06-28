"""Structured wordle game!!!"""

__author__ = "730462090"


def contains_char(any_string: str, single_chr: str) -> bool:
    """Checks for existence of second parameter string in first parameter string."""
    # Searches any_string for existence of single_chr through a loop.
    # Rseturns True if chr is found, else it returns False.
    assert len(single_chr) == 1
    index_check: int = 0
    while index_check < len(any_string):
        if single_chr == any_string[index_check]:
            return True
        else:
            index_check = index_check + 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Returns different colored boxes depending on if characters match in secret word."""
    # Utilizes contain_char function to check if either True or False was returned.
    # If true is returned, checks if position is exactly matching (Green box), if not it adds yellow box.
    # If false is returned, adds white box to string.
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    color_boxes: str = ""
    checker: int = 0
    while checker < len(secret_word):
        if contains_char(secret_word, user_guess[checker]) is True:
            if user_guess[checker] == secret_word[checker]:
                color_boxes = color_boxes + GREEN_BOX
            else:
                color_boxes = color_boxes + YELLOW_BOX
        else:
            color_boxes = color_boxes + WHITE_BOX
        checker = checker + 1
    return color_boxes


def input_guess(len_of_word: int) -> str:
    """Asks user for a guess of the secret word and stores final guess in a variable."""
    # Prompts user for an input guess with a specific amount of characters.
    # If incorrect length word is given, prompts user again until correct length word is given.
    # Stores last correct guess in variable and returns that variable.
    user_guess: str = input(f"Enter a {len_of_word} character word: ")
    while len(user_guess) != len_of_word:
        user_guess = input(f"That wasn't {len_of_word} chars! Try again: ")
    return(user_guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_wd: str = "codes"
    state: int = 1
    while state <= 6:
        # Utilizes input_guess and emojified function to set up wordle interface.
        # Loop will continue until user guesses secret word/user runs out of tries.
        print(f"=== Turn {state}/6 ===")
        user_guess = input_guess(5)
        box_string = emojified(user_guess, secret_wd)
        print(box_string)
        if user_guess == secret_wd:
            # If user guesses word before loop finishes, state variable will be set to 6 to exit from loop.
            print(f"You won in {state}/6 turns")
            state = 6
        state = state + 1
    if user_guess != secret_wd:
        # After loop has finished, means user has run out of tries and has not guessed word correctly. 
        # Ending message will be printed.
        print("X/6 - Sorry, try again tomorrow!")
    
    
if __name__ == "__main__":
    main()