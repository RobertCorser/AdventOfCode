#!/usr/bin/python3

floor = 0
enteredBasement = False

# Manually input parentheses
# print("Please enter parentheses")
# input = input()

#Read parentheses from file
input_file = open('/home/user/Downloads/Misc/AoC/input_1-1', 'r')
input = input_file.read()

for index, char in enumerate(input, start=1):
    if char == '(':
        floor += 1
    if char == ')':
        floor -= 1

    if floor == -1 and not enteredBasement:
        print("Santa first entered the basement at index {}".format(index))
        enteredBasement = True

print("Santa will end up on floor {}".format(floor))
