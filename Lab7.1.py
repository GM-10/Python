m1=[[1,2,3],[4,5,6]]
m2=[[7,8],[9,10],[11,12]]
res=[]
for i in range(0,len(m1)):
   temp=[]
   for k in range(0,len(m2[0])):
      ans=0
      for j in range(0,len(m2)):
         ans+=(m1[i][j])*(m2[j][k])
      temp.append(ans)
   res.append(temp)
print(res)
