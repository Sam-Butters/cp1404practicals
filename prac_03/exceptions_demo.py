"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When a letter is entered instead of a number, or a float instead of an integer.
2. When will a ZeroDivisionError occur?
    When the denominator is entered as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding a valid number loop which does not allow an input of zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
