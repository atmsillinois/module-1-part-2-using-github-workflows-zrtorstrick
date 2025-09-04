"""
This module implements the first HW assignment for UIUC, ATM 523, Fall 2025.

Module 1 Homework
ATMS 523
Fall 2025
Zachary Torstrick
"""

from sum import sum_of_integers


def main():
    """
    Prompt the user for two integers and print the result of sum_of_integers.

    The function handles:
    - ValueError: if input cannot be converted to int
    - TypeError: if sum_of_integers raises an error due to invalid input types
    """
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        result = sum_of_integers(a, b)
        print(f"The sum of {a} and {b} is {result}")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return
    except TypeError as e:
        print(str(e.args[0]))


if __name__ == "__main__":
    main()
