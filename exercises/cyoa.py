"""Choose your own adventure game!!!"""

__author__ = "730462090"

player = ""
points: int = 0
NAMED_CONSTANT: str = "\U00000000"
# from exercises.cyoa import main

def main() -> None:
    greet()
    player_choice: str = input("If you want to play the number game type NUMBER or if you want to play the coin game type COIN: ")
    while player_choice == "NUMBER" or "COIN" or "EXIT":
        if player_choice == "NUMBER":
            global points
            points = random_game(points)
            print(f"You have earned a total of {points} points!!")
            print(NAMED_CONSTANT)
            print("Congrats for making it through the game. Would you like to try the next game for a chance to earn more points?")
            player_choice = input("If you want to move to the next game type COIN or to replay the same game type NUMBER. To exit the adventure type EXIT. ")
            
        if player_choice == "COIN":
            coin_game()
            print(NAMED_CONSTANT)
            print("Congrats for making it through the game. Would you like to try the next game for a chance to earn more points?")
            player_choice: str = input("If you want to move to the next game type NUMBER or to replay the same game type COIN. To exit the adventure type EXIT: ")
        
        if player_choice == "EXIT":
            print("Hope you had fun in your adventure. Be sure to come back another time :))")
            return



def greet() -> None:
    print("===Welcome to the Choose your own adventure game!!===")
    global player
    player = input("What is your name? ")
    print(f"Hi {player}, today you have a choice of two exciting games!!")
    print("The first game is a guess the number game where you have to guess a random number from 1-10.")
    print("You will earn points based on how many tries it takes you to guess the number correctly.")
    print("The second game is a coin-flip game where you are asked to guess if the coin landed on Heads or Tails.")
    print("You will earn points based on how many times in a row you guess the correct flip." )
    


def hint(secret_number: int) -> int:
    hint_points = 0   
    smiling_monkey: str = "\U0001F648"
    want_hint: str = input(f"Would you like a hint {smiling_monkey}? You will loose 5 points if you chose to use it. Type YES or NO. ")
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


def random_game(points: int) -> int:
    from random import randint
    disappointed_face: str = "\U0001F623"
    party_face: str = "\U0001F973"
    secret_number: int = randint(1,10)
    guess_tracker: list[int] = list()
    global player
    print(NAMED_CONSTANT)
    print("===WELCOME TO THE NUMBER GUESSING GAME!!!=====")
    user_guess: int = int(input(f"What is your first guess {player}? "))
    guess_tracker.append(user_guess)
    

    while user_guess != secret_number:
        user_guess = int(input(f"Oh nooooo {disappointed_face} {player} That was not the correct number. Try again: "))
        guess_tracker.append(user_guess)
        if len(guess_tracker) == 5:
            print(f"Oh nooooo {disappointed_face} That was not the correct number.")
            points += hint(secret_number)
            user_guess = int(input("What is your guess? "))
            guess_tracker.append(user_guess)
    if user_guess == secret_number:
        number_tries: int = len(guess_tracker)
        if number_tries > 1:
            print(f"Congratulations {player} {party_face}!!!! You got my secret number in {number_tries} tries")
            if number_tries <= 5:
                points += 25
                return points
            else:
                points += 10
                return points
        else:
            points += 50
            print(f"Congratulations {player} {party_face}!!!! You got my secret number in 1 try!!")
            return points
        

def coin_game() -> None:
    print(NAMED_CONSTANT)
    print("===WELCOME TO THE COIN FLIP GAME!!===")
    
    party_face: str = "\U0001F973"
    cool_face: str = "\U0001F60E"
    sad_face: str = "\U0001F629"
    smug_face: str = "\U0001F92D"
    
    import random
    outcomes_list = ["Tails", "Heads"]
    flip_result = random.choice(outcomes_list)
    global points
    global player
    checker: int = 0
    user_guess: str = input("Heads or Tails? ")
    
    while user_guess == flip_result:
        print(f"Correct!!! {cool_face} The coin landed on {flip_result}.")
        flip_result = random.choice(outcomes_list)
        user_guess = input("See if you can keep the lucky streak :) Heads or Tails? ")
        checker += 1
    if checker > 1:
        print(f"Whoops!! The coin actually landed on {flip_result}.")
        print(f"You mangaged to guess the correct answer {checker} times in a row {player} {party_face}!!")
        checker = checker * 10
        points = points + checker
        print(f"You have earned a total of {points} points!!")
        return
    else:
        if checker == 1:
            print(f"Whoops!! The coin actually landed on {flip_result}.")
            print(f"Aww no {player} {sad_face} Your lucky streak only lasted for {checker} turn")
            checker = checker * 10
            points = points + checker
            print(f"You have earned a total of {points} points!!")
            return
        else:
            print(f"Whoops!! The coin actually landed on {flip_result}.")
            print(f"Aww no {player} {sad_face} Better luck next time.")
            print(f"You have earned a grand total of {points} points {smug_face}.")
            return

        
if __name__ == "__main__":
  main()