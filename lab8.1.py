class Person():
   def __init__(self, name, age):
        self.name = name
        self.age = age
   def Age(self):
       print("Age: ", self.age)
 
   def show(self):
      print("This is class person")
obj = Person("Jason", 35)
print("Name: ", obj.name)
obj.Age()
obj.show()
