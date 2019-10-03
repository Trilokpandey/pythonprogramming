#######operator overloading and dunder method############
#if repr method will only exist,it will print its own content even we ask for str(sonu)
#if str will exist then it'll first print its content if we write print(sonu)

class Employee:
    no_of_leaves=8#class variable
    def __init__(self,aname,aid,asalary):
        self.name=aname
        self.id=aid
        self.salary=asalary

    def print_detail(self):
        return f"my name is {self.name}.my id is {self.id} and my salary is {self.salary}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"employee({self.name},{self.id},{self.salary})"

    def __str__(self):
        return f"my name is {self.name}.my id is {self.id} and my salary is {self.salary}"




sonu=Employee("trilok",1,234)
#monu=Employee("sharad",2,120)
#print(sonu+monu)
#print(sonu/monu)
print(sonu)
print(repr(sonu))