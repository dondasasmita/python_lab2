# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("Enter your name : ")
age = int(input("Enter your current age : "))

# variable to store value of number of years to 100
turnHundred = 100 - age

# get the current time
now = datetime.datetime.now()

#
yearTurnHundred = now.year + turnHundred

print("Your name is " + name)
print("You will turn 100 year old in " + str(yearTurnHundred))

