#if we have to handle the missing values in ds or ml application then we have to use a slice operator inside the list datatype to get the desired value.
n=int(input("Enter the nu,ebr of lines you want: "))
for i in range (1,n+1):
   for j in range(1,i+1):
      if i%2==0:
         ch=64+j
         print(chr(ch),end='')
      else:
         print(j,end='')
   print('\n')    

   
