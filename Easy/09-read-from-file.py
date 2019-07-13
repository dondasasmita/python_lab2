# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen

names = []

with open("Files/names.txt", "r") as open_file:
    line = open_file.readline()
    while line:
        names.append(line.rstrip("\n\r"))
        line = open_file.readline()


# function to find the unique names
def findUniqueNames(list):
    unique_names = []
    for x in list:
        if x not in unique_names:
            unique_names.append(x)
    return unique_names


unique_names = findUniqueNames(names)
count = dict()

for x in unique_names:
    counter = 0
    for y in names:
        if y == x:
            counter += 1
    count[x] = counter

print(count)
