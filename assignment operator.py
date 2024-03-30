a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
while True:
   print("-"*30)
   print("1-Increment in a")
   print("2-Decrement in a")
   print("3-multiply b and a and store it in a ")
   print("4-divide a and b and store it in a ")
   print("5-exit")
   print("-"*30)
   ch=int(input("Enter your choice: "))
   if ch==1:
      a+=b
      print("a is ",a)
   elif ch==2:
      a-=b
      print("a is ",a)
   elif ch==3:
      a*=b
      print("a is ",a)
   elif ch==4:
      a/=b
      print("a is ",a)
   else:
      print("Thank you ")
      break
