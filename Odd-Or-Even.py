
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


if __name__ == '__main__':
    number = int(input("Please Enter a Number: "))

    if number % 2 == 0:
        print("{} is an Even Number".format(number))
    else:
        print("{} is an Odd Number".format(number))

    # Extra
    if number % 4 == 0:
        print("{} is Multiple of 4 ".format(number))

    num = int(input("Please enter a  number: "))
    check = int(input("Please enter another number: "))

    if num % check == 0:
        print("{} is Evenly divisible by {} ".format(num, check))
    else:
        print("{} is NOT Evenly divisible by {} ".format(num, check))