###########generator#########

'''
iterable- __iter__()  or __getitem__() [string is iterable]
iterator- __next__() #this will generate value one by one
iteration-
'''

#range is a generator which iterate only once
#generator is an iterator which iterate only once
#for i in range(50):
#    print(i)

def gen(n):
    for i in range(n):
        yield i


g=gen(2)
#print(g.__next__())
#print(g.__next__())
#print(g.__next__()) exceeding range

for i in g:
    print(i)


h="sonu"
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

'''
#this will give error as 'int' object is not iterable
m=123
ier=iter(m)
print(ier.__next__())

'''
