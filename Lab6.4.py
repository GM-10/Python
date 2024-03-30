a=eval(input("Enter the list:"))
print("The list is: ",a)
rem=[0,2,4,5]
for i in sorted(rem,reverse=True):
   print(i)
   del a[i]
print(a)
