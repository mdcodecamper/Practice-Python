""" Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old."""
""""
Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))

currentYear = 2018
tooBeOld = str((currentYear - age) + 100)

message = ""
message+= name + ", You are going to 100 years old in Year" + tooBeOld + "."

repeat = int(input("Please Enter How many times you want to print the message: "))


print(repeat * message)

print(repeat * message + "\n")
