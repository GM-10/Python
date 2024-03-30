import math
a=int(input("Enter the x coordinate of the center: "))
b=int(input("Enter the y coordinate of the center: "))
rad=int(input("Enter the radius: "))
x=int(input("Enter the x coordinate of the given point: "))
y=int(input("Enter the x coordinate of the given point: "))
ans=pow(pow((x-a),2)+ pow((y-b),2),0.5)
if ans==rad:
   print("Point lies on the circumference of the circle.")
elif ans>rad:
   print("Point lies outside the circle.")
else:
   print("Point lies inside the circle.")
