#lambda function or anonymous function

#def add(a,b):
#    return a+b

#minus=lambda x,y:x-y

#def minus(x,y):
#    return x-y

#print(minus(9,6))
'''
def list_return(abc):
    return abc[1]

abc=[[2,9],[5,4],[1,6]]
abc.sort(key=list_return)
print(abc)

'''
abc=[[2,9],[5,4],[1,6]]
abc.sort(key=lambda x:x[1])
print(abc)
