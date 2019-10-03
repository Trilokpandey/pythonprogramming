class Employee:
    no_of_leaves=8#class variable
    def __init__(self,aname,aid,aroll):
        self.name=aname
        self.id=aid
        self.roll=aroll

    def print_detail(self):
        return f"my name is {self.name}.my id is {self.id} and my roll is {self.roll}"

sonu=Employee("trilok",1,234)
#monu=Employee()

#sonu.name="trilok"
#sonu.id=1
#sonu.roll=234

#monu.name="sharad"
#monu.id=2
#monu.roll=2134

#print(monu.print_detail())

print(sonu.name)
print(sonu.print_detail())