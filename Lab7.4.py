f=open('a.txt','r')
f1=open('b.txt','a')
temp=(f.read())
f1.write(temp)


f.close()
f1.close()
