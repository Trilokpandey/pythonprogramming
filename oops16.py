############Object Introspection####################

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"my name is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        print("setting now...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

sonu=Employee("sonu","pandey")
print(type(sonu))
print(id(sonu))
print(type("hello guys"))
print(id("hello guys"))
print(id("hello "))
m="hello guys"
print(dir(m))
print(dir(sonu))

import inspect
print(inspect.getmembers(sonu))