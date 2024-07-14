def multiplication_table():
    """
    This function generates and prints a multiplication table for a given number.
    """

    number = int(input("Enter a number to see its multiplication table: "))

    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")


if __name__ == "__main__":
    multiplication_table()