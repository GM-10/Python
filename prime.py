a=int(input("Enter a number: "))
count=0
for i in range(2,a,1):
   if (a%i==0):
      print("Not a prime number.")
      break
   else:
      count+=1
if count==(a-2):
   print("Prime number.")
   
