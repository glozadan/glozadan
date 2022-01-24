# This program computes the area of circles and triangles

print "The program is starting!"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Please enter the radius: "))
  area = 3.14159 * (radius**2)
  print "The area of the circel is: ", str(area)+"u^2"
elif option == 'T':
  base = float(raw_input("Please enter the length of the base: "))
  height = float(raw_input("Please enter the height of the triangle: "))
  area = (base * height)/2
  print "The area of the triangle is: ", str(area)+"u^2"
else:
  print "Invalid shape! Please try again"

print "The program is exiting"
