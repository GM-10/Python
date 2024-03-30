count=0
str1=input("Enter string: ")
for i in str1:
   print(i)
   if i =="a":
      count=count+1
   elif i=="A":
      count=count+1
   else:
      pass
print("The frequency of A or a is ",count)
