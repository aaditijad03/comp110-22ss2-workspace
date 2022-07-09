"""Example of writing a function to process a list."""

def main() -> None:
    """Entry point of program"""
    names: list[str] = ["Mark", "Johnny", "Lisa", "Jennie"]
    print(contains("Lisa", names))

def contains(needle: str, haystack: list[str]) -> bool:
    """Return true if needle is found in haystack, False otherwise"""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False

if __name__ == "__main__":
    main()