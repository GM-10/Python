lst=[4,6,6,4,2,2,4,8,5,8]
val=dict()
for i in lst:
   a= val.keys()
   if i in a:
      val[i].append(i) 
   else:
      val[i]=[i]
print(val)
      
