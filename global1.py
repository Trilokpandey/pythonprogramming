
'''
a=10

def fun1(n):
    #a=5
    m=7
    global a
    a=a+50
    print(a,m)
    print(n,"hi")
fun1("hello")
print(a)

'''
x=60
def pandey():
    x=20
    def sonu():
        global x
        x=80
    print("before calling sonu()",x)
    sonu()
    print("before calling sonu()", x)

pandey()
print(x)
