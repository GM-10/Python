class employee():
   def hello_employee(self, name=None):
      if name is not None:
         self.name = name
         print("Hello $"+self.name+" $")
      else:
         print("Hello")
obj=employee()
obj.hello_employee()
obj.hello_employee("Jacob")
