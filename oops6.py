#static method

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

    @classmethod
    def from_dash(cls,str):
        params=str.split("-")
        print(params)
        return cls(params[0],params[1],params[2])

    @classmethod
    def from_slash(cls,str):
        return cls(*str.split("/"))

    @staticmethod
    def print_good(str):
        print("who is good boy " +str)




sonu=Employee("trilok",1,234)
monu=Employee("sharad",2,120)
#ayush=Employee.from_dash("ayush-11-220")
#raju=Employee.from_slash("raju/20/1020")

sonu.print_good("trilok")
#print(ayush.roll)
#print(raju.name)