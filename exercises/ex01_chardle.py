"""EX1 - Chardle!"""

__author__ = "730462090"

num_of_times: int = 0
five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for " + single_character + " in " + five_character_word)
        
        if single_character == five_character_word[0]:
            print(single_character + " found at index 0")
            num_of_times = num_of_times + 1
        if single_character == five_character_word[1]:
            print(single_character + " found at index 1")
            num_of_times = num_of_times + 1
        if single_character == five_character_word[2]:
            print(single_character + " found at index 2")
            num_of_times = num_of_times + 1
        if single_character == five_character_word[3]:
            print(single_character + " found at index 3")
            num_of_times = num_of_times + 1
        if single_character == five_character_word[4]:
            print(single_character + " found at index 4")
            num_of_times = num_of_times + 1

        if num_of_times == 1:
            print(str(num_of_times) + " instance of " + single_character + " found in " + five_character_word)
        else:
            if num_of_times > 1:
                print(str(num_of_times) + " instances of " + single_character + " found in " + five_character_word)
            else:
                if num_of_times == 0:
                    print("No instances of " + single_character + " found in " + five_character_word)








    
