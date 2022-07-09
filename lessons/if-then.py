"""Practice with if-then-else statements"""

choice: int = int(input("Enter a number: "))

# A when c < 25
# B when c >= 25 and < 50
# C when c > 75
# D when c >= 50 and <= 75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")
