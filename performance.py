per=int(input("Enter the percentage of the student: "))
if (per>=90):
   print("Excellent performance.")
elif (per>=80 and  per<90):
   print("Very Good performance.")
elif (per>=70 and  per<80):
   print("Good performance.")
elif (per>=60 and  per<70):
   print("Average performance.")
else:
   print("Poor performance.")
