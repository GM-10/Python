a=eval(input("Enter the list:"))
print("The list is: ",a)
x=int(input("Enter the element you want to remove: "))
for ele in a:
   if ele==x:
      a.remove(ele)

print(a)
