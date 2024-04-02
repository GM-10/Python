class Person():
   def show(self):
      print("Using super you can call this function.")
class Student(Person):
   def show(self):
      super().show()
      print("Derived class")
a=Student()
a.show()
