# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

length = 20.5
width = 10.25
height = 5.5

surface_area = 2 * (length+height+width)
print("Surface Area: ", surface_area)

volume = length * width * height
print("Volume: ", volume)