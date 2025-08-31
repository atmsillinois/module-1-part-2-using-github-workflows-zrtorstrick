"""
Accept two integers
Print their values
Print their sum or error running sum function
"""

from sum import sum_of_integers


def main():
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
