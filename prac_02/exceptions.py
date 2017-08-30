"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when a float is entered
2. When will a ZeroDivisionError occur? when 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     while denominator == 0:
#             print("Cannot divide by zero, please enter another number")
#             denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print('Finished.')

def main():
    x = input(">>>")
    if blank_check(x,"title")
        x = blank_check(x,"title")
    print(x)


def blank_check(word,ask_for):
    while not word:
        print("Input can not be be blank")
        word = (input(ask_for))
    return word

main()