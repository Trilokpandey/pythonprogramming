#class -template
#object-instance of class
#DRY-don't repeat yourself

class Student:
    pass

sonu=Student()
monu=Student()

sonu.name="trilok"
sonu.roll=1193
sonu.section='a'
monu.subjects=["phy","maths"]
print(sonu)
print(monu)
print(sonu.name)
print(sonu.roll,monu.subjects)

