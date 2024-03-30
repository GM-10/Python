
def isPrime(a):
   res=1
   if (a==2):
      res=1
   else:
      for i in range(2,a):
         if(a%i==0):
            res=0
   return res




n=int(input("Enter the number you want to check: "))
res=isPrime(n)
print("The answer is",res)
