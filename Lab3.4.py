def isPal(str1):
   res=1
   for i in range(0,int(len(str1))):
      if(str1[i]!=str1[len(str1)-i-1]):
         res=0
   return res

string=input("Enter the string you want to check for: ")
ans=isPal(string)
if(ans==1):
   print("It is a palindrome.")
else:
   print("It is not a palindrome.")
