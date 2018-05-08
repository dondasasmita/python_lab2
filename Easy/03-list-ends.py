# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list.

numbers = input("Enter a few random number separated by comma  : ")
list = numbers.split(",")
newlist = [list[0], list[len(list)-1]]
print(newlist)


