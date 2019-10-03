#def function1():
#    print("chill!!it's sunday today")

#fun2=function1
#del function1
#fun2()
'''
def funret(num):
    if num==0:
        return print
    if num==1:
        return sum

a=funret(1)
print(a)
'''
#def executor(fun):
#    fun("hello")

#executor(print)

#############decorator########

def dec1(fun):
    def exec():
        print("executing now")
        fun()
        print("executed")
    return exec
@dec1
def print_name():
    print("my name is pandey")

#print_name=dec1(print_name)
print_name()