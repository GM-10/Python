def fact(a):
   res=1
   for i in range(1,a+1):
      res*=i
   return res





n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
if(n>r):
   nfac=fact(n)
   rfac=fact(r)
   nrfac=fact(n-r)
   ncr=nfac/(rfac*nrfac)
   npr=nfac/nrfac
   print("nCr value is: ",ncr)
   print("nPr value is: ",npr)
else:
   print("Enter valid numbers.")
