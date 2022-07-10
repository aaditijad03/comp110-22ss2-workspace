"""Dictionary related utility functions."""

__author__ = "730462090"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV file line by line
    for row in csv_reader:
        result.append(row)

    # Close file when done, to free its resources
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result