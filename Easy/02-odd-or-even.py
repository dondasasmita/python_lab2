# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


number = int(input("Enter a number : "))
if number % 2 == 0:
    print("You have entered an even number")
else:
    print("You have entered an odd number")
