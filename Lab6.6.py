def last(n):
   return n[1]

tuple1=(('a',23),('b',37),('c',11),('d',29))
print(sorted(tuple1,key=last))
print(type(last))
