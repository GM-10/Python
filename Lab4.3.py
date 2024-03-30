f1=open("file1.txt","r")
f2=open("file2.txt","r")
f3=open("file3.txt","w")
line1=f1.read()
line2=f2.read()
f3.write(line1+'\n'+line2)


f1.close()
f2.close()
f3.close()
