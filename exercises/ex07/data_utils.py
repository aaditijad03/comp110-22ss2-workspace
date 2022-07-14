"""Dictionary related utility functions."""

__author__ = "730462090"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads csv rows when given a file."""
    from csv import DictReader
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-orientated table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data_table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Returns revised datatable with an inputted number of rows."""
    empty_dict = {}
    for item in data_table:
        if row_num >= len(data_table[item]):
            return data_table
        empty_list = []
        i = 0
        while i < row_num:
            empty_list.append(data_table[item][i])
            i += 1
        empty_dict[item] = empty_list
    return empty_dict


def select(data_table: dict[str, list[str]], subset: list[str]) -> dict[str, list[str]]:
    """Returns a subset of the datatable when given specific strings."""
    empty_dict = {}
    for item in subset:
        empty_dict[item] = data_table[item]
    return empty_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a concatenated table with inputs from both parameters."""
    empty_dict = {}
    for column in table_1:
        empty_dict[column] = table_1[column]
    for column in table_2:
        if column in empty_dict:
            empty_dict[column] += table_2[column]
        else:
            empty_dict[column] = table_2[column]
    return empty_dict


def count(list: list[str]) -> dict[str, int]:
    """Returns the count of each item in a list and stores values in a dictionary."""
    blank_dict = {}
    for item in list:
        if item not in blank_dict:
            blank_dict[item] = 1
        else:
            blank_dict[item] += 1
    return blank_dict