class Employee:
    no_of_leaves=8#class variable
    pass

sonu=Employee()
monu=Employee()
sonu.name="trilok"
sonu.id=1
sonu.roll=234
monu.name="sharad"
monu.id=2
monu.roll=2134
print(Employee.__dict__)
print(monu.no_of_leaves)
print(sonu.no_of_leaves)
Employee.no_of_leaves=10
print(Employee.__dict__)
monu.no_of_leaves=5 #instance variable
print(monu.no_of_leaves)
print(sonu.no_of_leaves)
print(monu.__dict__)
print(sonu.__dict__)



