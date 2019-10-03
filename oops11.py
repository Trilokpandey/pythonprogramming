############polymorphism###############
#print(5+6)
#print("5"+"6")

##########overiding and super#########

#when we access any variable,it'll look for instance variable first
#order of super is very important,program continue after super according it print
class A:
    classvar1="i am a class variable in A"
    var=5
    def __init__(self):
        self.var1="i am instance variable in A"
        self.classvar1="i am instance variable in A"
        self.special="special "

class B(A):
    classvar2="i am a class variable in B"
    classvar1="i am class variable in B"
    def __init__(self):
        #super().__init__()
        self.var1="i am instance variable in B"
        self.classvar1="i am instance variable in B"
        super().__init__()
        print(super().classvar1)
        print(super().var)

a=A()
b=B()
#print(b.classvar1)
print(b.special,b.var1,b.classvar1)
#print(b.classvar1)