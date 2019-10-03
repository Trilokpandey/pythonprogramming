#to demonstrate how we can change class instance value with instance variable
#if any instance value will change the class instance value,it'll reflect for all instance value

class Employee:
    no_of_leaves=8#class variable
    def __init__(self,aname,aid,aroll):
        self.name=aname
        self.id=aid
        self.roll=aroll

    def print_detail(self):
        return f"my name is {self.name}.my id is {self.id} and my roll is {self.roll}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


sonu=Employee("trilok",1,234)
monu=Employee("sharad",2,120)

#sonu.no_of_leaves=6
#print(sonu.no_of_leaves)
#print(monu.no_of_leaves)
#print(sonu.print_detail())
#Employee.no_of_leaves=60
#print(monu.no_of_leaves)

sonu.change_leaves(100)
print(sonu.no_of_leaves)
print(monu.no_of_leaves)