ms=(input("Enter marital status: "))
gen=(input("Enter gender: "))
age=int(input("Enter age: "))
if(ms=='Y'):
   print("Eligible for insurance.")
elif(ms=='N' and gen=='M' and age>30):
   print("Eligible for insurance.")
elif(ms=='N' and gen=='F' and age>25):
   print("Eligible for insurance.")
else:
   print("Not eligible.")
