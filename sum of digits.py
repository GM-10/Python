a=int(input("Enter a number: "))
b=a
n=0
while b>0:
   b=b//10
   n=n+1
b=x=a
sum1=ans=count=0
while b>0:
   b%=(10**(n-1))
   x=x-b
   sum1=(x//(10**(n-1)))
   ans=sum1*10**(n-count-1)
   n=n-1
   x=b
   count+=1
   print(ans)
   
