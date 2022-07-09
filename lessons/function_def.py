"""An example function definition."""

def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    
    return b

"""python -m lessons.function_def"""

x: int = 6
y: int = 5 + 2
z: int = my_max (x,y)
print(z)
