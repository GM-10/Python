lst=[4,6,2,1,6,7,4]
unqlst=[]
lst.sort()
for i in range(0,len(lst)):
   if (lst[i]!= lst[i-1]):
      unqlst.append(lst[i])
print("Non duplicate list : ",unqlst)
