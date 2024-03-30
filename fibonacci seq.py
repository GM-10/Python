length=16
x=0
y=1
iteration=0
if length<=0:
   print("Please provide a number greater than zero.")
elif length==1:
   print("The fibonacci sequence has {} element".format(length),":")
   print(x)
else:
   print("This fibonacci sequence has {} element".format(length),":")
while(iteration<length):
   print(x, end=',')
   z=x+y
   x=y
   y=z
   iteration+=1
