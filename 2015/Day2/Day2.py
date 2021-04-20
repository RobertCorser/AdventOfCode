#!/usr/bin/python3

total = 0
slack = 0
surfaceArea = 0
totalWrappingPaper = 0
totalRibbon = 0

# Get dimensions of box
# print("Please input the dimensions in the format \'l*w*h\'")
# input = input()

file = open("/home/user/Downloads/Misc/AoC/input_2", "r")
input = file.readlines()

# Process the inputs
for line in input:

    surfaceArea = 0

    length, width, height = line.split('x')

    # Calculate the surface area for each side, track the smallest side
    # Calculate the smallest perimeter and use that as the ribbon length
    temp = int(length) * int(width)
    smallestSide = temp
    temp *= 2
    surfaceArea += temp
    tempPerimeter = (2 * int(length)) + (2 * int(width))
    smallestPerimeter = tempPerimeter

    temp = int(width) * int(height)
    if temp < smallestSide:
        smallestSide = temp
    temp *= 2
    surfaceArea += temp
    tempPerimeter = (2 * int(width)) + (2 * int(height))
    if tempPerimeter < smallestPerimeter:
        smallestPerimeter = tempPerimeter

    temp = int(height) * int(length)
    if temp < smallestSide:
        smallestSide = temp
    temp *= 2
    surfaceArea += temp
    tempPerimeter = (2 * int(height)) + (2 * int(length))
    if tempPerimeter < smallestPerimeter:
        smallestPerimeter = tempPerimeter

    # print("Length: {len}\nWidth: {wid}\nHeight: {hei}\n".format(len=length, wid=width, hei=height))
    # print("Smallest side: {smol}\nSubtotal Surface Area: {subArea}\n".format(smol=smallestSide, subArea=surfaceArea,))

    # Add the smallest side (in terms of area) to account for slack paper
    surfaceArea += smallestSide

    # print("Total Surface Area (including slack):{}".format(surfaceArea))

    # Keep track of total amount of wrapping paper across all boxes
    totalWrappingPaper += surfaceArea

    # Add the bow, (which is equal to the cubic volume of the box) to the smallest perimeter to get total ribbon for box
    smallestPerimeter += int(length) * int(width) * int(height)
    # Keep track of total amount of ribbon across all boxes
    totalRibbon += smallestPerimeter

print("The total amount of wrapping paper needed is {} sq ft.".format(totalWrappingPaper))
print("The total amount of ribbon needed is {} sq ft.".format(totalRibbon))

