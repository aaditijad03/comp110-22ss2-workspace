"""Dictionary functions!!"""

__author__ = "730462090"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts items in a dictionary."""
    blank_dict = {}
    blank_list = []
    i: int = 0
    counter: int = 1
    for item in dictionary:
        blank_list.append(dictionary[item])
    while i < len(blank_list):
        while counter < len(blank_list):
            if blank_list[i] == blank_list[counter]:
                raise KeyError("Oh No!! Looks like your dictionary contains two of the same values.")
            counter += 1
        i += 1
        counter = i + 1
    for item in dictionary:
        temp: str = item
        value: str = dictionary[item]
        blank_dict[value] = temp
    return blank_dict
    

def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns value that appears the most in the dictionary."""
    colors_list = []
    reverse_dict = {}
    values_list = []
    for item in dictionary:
        colors_list.append(dictionary[item])
    dict_values: dict = count(colors_list)
    for item in dict_values:
        temp: str = item
        value: str = dict_values[item]
        reverse_dict[value] = temp
    for item in reverse_dict:
        values_list.append(item)
    highest_value: int = values_list[0]
    for item in values_list:
        if item > highest_value:
            highest_value = item
    return reverse_dict[highest_value]
    

def count(list: list[str]) -> dict[str, int]:
    """Returns the count of each item in a list and stores values in a dictionary."""
    blank_dict = {}
    for item in list:
        if item not in blank_dict:
            blank_dict[item] = 1
        else:
            blank_dict[item] += 1
    return blank_dict