def pattern_drawing():
    """
    This function draws a square pattern of asterisks based on user input.
    """

    size = int(input("Enter the size of the pattern: "))

    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end="")
            col += 1
        print()  # Print a newline to move to the next row
        row += 1


if __name__ == "__main__":
    pattern_drawing()