# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!

def find_max(num1, num2, num3):
    max = 0
    if num1 > num2 and num1 > num3:
        max = num1
    if num2 > num1 and num2 > num3:
        max = num2
    elif num3 > num1 and num3 > num2:
        max = num3
    return max


print(find_max(50, 75, 100))