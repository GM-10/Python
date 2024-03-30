def g(x):
   def h(x):
      x='abc'
   x=x+1
   print('in g(x): x= ',x)
   h(x)#after adding the argument in h
   return x
x=3
z=g(x)
