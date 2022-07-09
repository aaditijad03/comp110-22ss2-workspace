"""Dictionary functions tests."""

__author__ = "730462090"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count


def test_invert_blank() -> None:
    """Tests if function will return a blank dictionary when given a blank dictionary."""
    blank_dict = {}
    assert invert(blank_dict) == {}


def test_invert_single_item() -> None:
    """Tests if invert can work with just one row in a dictionary."""
    single_test = {"a": "b"}
    assert invert(single_test) == {"b": "a"}


def test_invert_multiple_items() -> None:
    """Tests if invert can invert multiple items in a dictionary."""
    multiple_dict = {"a": "b", "c": "d"}
    assert invert(multiple_dict) == {"b": "a", "d": "c"}


def test_count_blank() -> None:
    """Tests if count will return a blank dictionary when given a blank list."""
    blank_list = []
    assert count(blank_list) == {}


def test_count_single_item() -> None:
    """Tests if it can count 1 item."""
    ex_list = ["a"]
    assert count(ex_list) == {"a": 1}


def test_count_capital() -> None:
    """Tests if count works with capital strings."""
    ex_list = ["A", "B", "A"]
    assert count(ex_list) == {"A": 2, "B": 1}


def test_count_multiple_items() -> None:
    """Tests if count can work with multiple items."""
    ex_list = ["a", "b", "a", "a", "c", "b"]
    assert count(ex_list) == {"a": 3, "b": 2, "c": 1}


def test_favorite_color_single_item() -> None:
    """Tests if fav_color can work with just one item."""
    ex_dict = {"Aaditi": "grey"}
    assert favorite_color(ex_dict) == "grey"


def test_favorite_color_multiple_items() -> None:
    """Tests if favorite color can work with multiple items."""
    ex_dict = {"aaditi": "grey", "ridhi": "purple", "anika": "purple"}
    assert favorite_color(ex_dict) == "purple"


def test_favorite_color_capital() -> None:
    """Tests if favorite color can work with Capital strings."""
    ex_dict = {"Aaditi": "GREY", "Ridhi": "PURPLE", "Anika": "PURPLE", "Mayra": "GREEN", "Jay": "GREEN", "Lila": "PURPLE"}
    assert favorite_color(ex_dict) == "PURPLE"