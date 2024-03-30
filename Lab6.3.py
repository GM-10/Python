lst1=eval(input("Enter the list1:"))
print("The list1 is: ",lst1)
lst2=eval(input("Enter the list2:"))
print("The list2 is: ",lst2)
x=False
for a in lst1:
   for b in lst2:
      if a==b:
         x=True
print("Ths answer is: ",x)
