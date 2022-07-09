"""List utility functions!"""

__author__ = "73062090"


def only_evens(evens: list[int]) -> list[int]:
    """Returns only the even numbers from a given list."""
    evens_list = list()
    for match in evens:
        if match % 2 == 0:
            evens_list.append(match)
    return evens_list


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns True if two lists match each other exactly, otherwise returns False."""
    if len(list_1) != len(list_2):
        return False
    i: int = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def sub(main_list: list[int], index_1: int, index_2: int) -> list[int]:
    """Returns a subset of a inputted list between 2 inputted indexes."""
    sub_list = list()
    if len(main_list) == 0 or index_1 > len(main_list) or index_2 <= 0:
        return sub_list
    if index_1 < 0:
        index_1 = 0
    if index_2 > len(main_list):
        index_2 = len(main_list)
    while index_1 < index_2:
        sub_list.append(main_list[index_1])
        index_1 += 1
    return sub_list