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