'''
def function_name_print(a,b,c):
    print(a,b,c)
function_name_print("raju","rohan","raman")

we need to pass another argument when we desire to print new name
'''
#convention:*args parameter must be last argument else it'll give error
'''
def function_name_print(abc,*args):
    print(abc)
    print(type(args))
    for item in args:
        print(item)


name=["raju","rohan","raman","sonu"]
abc=20
function_name_print(abc,*name)
'''
#note:kwargs can be used to handle the above restriction of args
def function_name_print(abc,*args,**kwargs):
    print(abc)
    print(type(args))
    print(type(kwargs))
    for item in args:
        print(item)
    print("here we'll get info through kwargs")
    for key,value in kwargs.items():
        print(f"{key} is {value}.")


name=["raju","rohan","raman"]
abc=20
kw={"rahul":"cook","ayush":"programmer","shiva":"trainer"}
function_name_print(abc,*name,**kw)


xyz={'a':1,'b':2,'c':3}
print(xyz.items())
for key,value in xyz.items():
    print(key)
    print(value)
