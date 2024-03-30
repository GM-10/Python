a=int(input("Enter start number:"))
b=int(input("Enter end number:"))
lst=[]
for i in range (a,b+1):
   if i%2!=0:
      lst.append(i)
lst.sort()
lst.reverse()
print(lst)
