a=int(input("Enter a number: "))
b=a
n=0
while b>0:
   b=b//10
   n=n+1
b=x=a
pw=n
ans=0
while b>0:
   b%=(10**(n-1))
   x=x-b
   ans=ans+(x//(10**(n-1)))**pw
   n=n-1
   x=b
if ans==a:
   print("Number is an armstrong number.")
else:
   print("Number is not an armstrong number.")
   
