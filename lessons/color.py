
def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts items in a dictionary."""
    blank_dict = {}
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
# from lessons.color import favorite_color
# favorite_color({"Marc": "red", "Ezri": "red", "Kris": "blue", "Addie": "green"})

def count(list: list[str]) -> dict[str, int]:
    """Returns the count of each item in a list and stores values in a dictionary."""
    blank_dict = {}
    for item in list:
        if item not in blank_dict:
            blank_dict[item] = 1
        else:
            blank_dict[item] += 1
    return blank_dict

def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns value that appears the most in the dictionary."""
    blank_list = []
    for item in dictionary:
        blank_list.append(dictionary[item])
    dict_values: dict = invert(count(blank_list))
    print(dict_values)
    values_list = []
    for item in dict_values:
        values_list.append(item)
    highest_value: int = values_list[0]
    for item in values_list:
        if item > highest_value:
            highest_value = item
    return dict_values[highest_value]