##############multiple inheritance##############

#constructor of that parent class will be called which comes first in the sequence of derive class


class Employee:
    no_of_leaves=18
    var=8
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

class Player:
    var=9
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print_gdetail(self):
        return f"name of player is {self.name} and he plays {self.game}"

class Coolprogrammer(Player,Employee):
    #var=25
    language = "c++"
    def print_language(self):
        print(self.language)


sonu=Employee("trilok",1,234)
monu=Employee("sharad",2,120)
#ayush=Coolprogrammer("ayush",18,43,)
anshu=Coolprogrammer("ayush",["cricket","football"])
#print(ayush.print_detail())
#print(ayush.var)
print(anshu.print_gdetail())
print(anshu.var)
