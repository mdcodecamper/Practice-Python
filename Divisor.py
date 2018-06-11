"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

if __name__ == '__main__':
    num = int(input("Please Enter a number: "))

    i = 1
    while (i <= num):
        if (num % i == 0):
            print(i)
        i += 1
