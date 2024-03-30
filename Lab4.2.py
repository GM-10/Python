x1=int(input("Enter the x coordinate of first point."))
y1=int(input("Enter the y coordinate of first point."))
x2=int(input("Enter the x coordinate of second point."))
y2=int(input("Enter the y coordinate of second point."))
x3=int(input("Enter the x coordinate of third point."))
y3=int(input("Enter the y coordinate of third point."))
if ((y2-y1)/(x2-x1)==(y3-y2)/(x3-x2)):
   print("points are collinear.")
else:
   print("points are not collinear.")
