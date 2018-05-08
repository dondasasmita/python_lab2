# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Solution :

# declare a new function to find num in list
def find_num_in_list(list,num_to_find):
    # using for loop to go through the numbers in list
  for num in list:
      if num == num_to_find:
          return True
  else:
        return False


myList = [1, 3, 5, 7, 9]
print(find_num_in_list(myList, 3))

