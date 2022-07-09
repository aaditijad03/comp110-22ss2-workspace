"""Choose your own adventure game!!!"""

__author__ = "730462090"

player: str = ""
points: int = 0
BLANK_SPACE: str = "\U00000000"
SMILING_MONKEY: str = "\U0001F648"
DISAPPOINTED_FACE: str = "\U0001F623"
PARTY_FACE: str = "\U0001F973"
COOL_FACE: str = "\U0001F60E"
SAD_FACE: str = "\U0001F629"
SMUG_FACE: str = "\U0001F92D"


def main() -> None:
    """Main function which controls which path user is set to. There are 2 adventure paths and 1 exit path."""
    greet()
    player_choice: str = input("If you want to play the number game type NUMBER or if you want to play the coin game type COIN: ")
    # Main game loop:
    while player_choice == "NUMBER" or "COIN" or "EXIT":
        if player_choice == "NUMBER":
            global points
            # Passes integer value of points as an argument into the custom function random_game:
            points = random_game(points)
            print(f"You have earned a total of {points} points!!")
            print(BLANK_SPACE)
            print("Congrats for making it through the game. Would you like to try the next game for a chance to earn more points?")
            player_choice = input("If you want to move to the next game type COIN or to replay the same game type NUMBER. To exit the adventure type EXIT. ")
            
        if player_choice == "COIN":
            # Custom procedure:
            coin_game()
            print(BLANK_SPACE)
            print("Congrats for making it through the game. Would you like to try the next game for a chance to earn more points?")
            player_choice: str = input("If you want to move to the next game type NUMBER or to replay the same game type COIN. To exit the adventure type EXIT: ")
        
        if player_choice == "EXIT":
            print(BLANK_SPACE)
            print(f"Once again congrats for earning {points} points!!")
            print("Hope you had fun in your adventure. Be sure to come back another time :))")
            return


def greet() -> None:
    """Function is responsible for printing welcome message and storing inputed player's name."""
    print("===Welcome to the Choose your own adventure game!!===")
    global player
    player = input("What is your name? ")
    print(f"Hi {player}, today you have a choice of two exciting games!!")
    print(BLANK_SPACE)
    print("The first game is a guess the number game where you have to guess a random number from 1-10.")
    print("You will earn points based on how many tries it takes you to guess the number correctly.")
    print(BLANK_SPACE)
    print("The second game is a coin-flip game where you are asked to guess if the coin landed on Heads or Tails.")
    print("You will earn points based on how many times in a row you guess the correct flip.")
    print(BLANK_SPACE)
    

def hint(secret_number: int) -> int:
    """Responsible for deducting points if hint is used or letting points stay the same."""
    hint_points = 0   
    want_hint: str = input(f"Would you like a hint {SMILING_MONKEY}? You will loose 5 points if you chose to use it. Type YES or NO. ")
    # Checks if user wants hint and gives a hint to the range of the secret number as hint.
    if want_hint == "YES":
        hint_points -= 5
        if secret_number > 5:
            print("The number I'm thinking of is greater than 5")
            return hint_points
        else:
            if secret_number <= 5:
                print("The number I am thinking of is 5 or smaller.")
                return hint_points
    if want_hint == "NO":
        return hint_points


# CUSTOM FUNCTION:
def random_game(points: int) -> int:
    """Responsible for adding points based on how many tries it takes the user to guess the correct number."""
    from random import randint
    secret_number: int = randint(1, 10)
    # List variable that keeps track of all user guesses; will be used to calculate total number of tries later.
    guess_tracker: list[int] = list()
    global player
    print(BLANK_SPACE)
    print("===WELCOME TO THE NUMBER GUESSING GAME!!!=====")
    user_guess: int = int(input(f"What is your first guess {player}? "))
    guess_tracker.append(user_guess)
    
    while user_guess != secret_number:
        user_guess = int(input(f"Oh nooooo {DISAPPOINTED_FACE} {player} That was not the correct number. Try again: "))
        guess_tracker.append(user_guess)
        if len(guess_tracker) == 5:
            print(f"Oh nooooo {DISAPPOINTED_FACE} That was not the correct number.")
            # Once the user reaches 5 guesses, calls the hint function and reassigns the point value if user chose to use hint or not.
            points += hint(secret_number)
            user_guess = int(input("What is your guess? "))
            guess_tracker.append(user_guess)
    # Once user guesses secret number correctly, exits out of loop and calculates points earned based on total tries.
    if user_guess == secret_number:
        number_tries: int = len(guess_tracker)
        if number_tries > 1:
            print(f"Congratulations {player} {PARTY_FACE}!!!! You got my secret number in {number_tries} tries")
            if number_tries <= 5:
                points += 25
                return points
            else:
                points += 10
                return points
        # If user gets secret number in first try, a special message is printed and number of points earned is the greatest.
        else:
            points += 50
            print(f"Congratulations {player} {PARTY_FACE}!!!! You got my secret number in 1 try!!")
            return points
        

# CUSTOM PROCEDURE:
def coin_game() -> None:
    """Responsible for adding points based on number of times in a row that the user guesses the correct outcome."""
    print(BLANK_SPACE)
    print("===WELCOME TO THE COIN FLIP GAME!!===")

    import random
    outcomes_list = ["Tails", "Heads"]
    flip_result = random.choice(outcomes_list)
    # Calls global variables to reassign values without returning a seperate value like the random_guess function
    global points
    global player
    checker: int = 0
    user_guess: str = input("Heads or Tails? ")
    # Loop will run until user guesses incorrect value, a checker variable will keep track of number of times loop ran.
    while user_guess == flip_result:
        print(f"Correct!!! {COOL_FACE} The coin landed on {flip_result}.")
        flip_result = random.choice(outcomes_list)
        user_guess = input("See if you can keep the lucky streak :) Heads or Tails? ")
        checker += 1
    # At this point user has guessed wrong, and program will exit out of loop and assign points based on checker value.
    if checker > 1:
        print(f"Whoops!! The coin actually landed on {flip_result}.")
        print(f"You mangaged to guess the correct answer {checker} times in a row {player} {PARTY_FACE}!!")
        checker *= 10
        points = points + checker
        print(f"You have earned a total of {points} points!!")
        return
    else:
        # If player only guesses correctly once, a separate message is printed.
        if checker == 1:
            print(f"Whoops!! The coin actually landed on {flip_result}.")
            print(f"Aww no {player} {SAD_FACE} Your lucky streak only lasted for {checker} turn")
            checker *= 10
            points = points + checker
            print(f"You have earned a total of {points} points!!")
            return
        # If first guess itself is wrong, a separate message is printed.
        else:
            print(f"Whoops!! The coin actually landed on {flip_result}.")
            print(f"Aww no {player} {SAD_FACE} Better luck next time.")
            print(f"You have earned a grand total of {points} points {SMUG_FACE}.")
            return

        
if __name__ == "__main__":
    main()