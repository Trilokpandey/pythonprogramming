'''
number=["2","34","64"]

#for item in range(len(number)):
 #   number[item]=int(number[item])

number=list(map(int,number))
print(number)

number[2]=number[2]+1
print(number[2])

def sq(x):
    return x*x
num=[2,3,4,5,6]
square=list(map(sq,num))
#square=list(map(lambda x:x*x,num))
print(square)


def square(a):
    return a*a

def cube(a):
    return a*a*a

fun=[square,cube]

for item in range(5):
    lst=list(map(lambda x:x(item),fun))
    print(lst)



#filter

num=[2,3,4,5,6]

def num_gt_4(number):
    return number>4

lst=list(filter(num_gt_4,num))
print(lst)

'''

#reduce
from functools import reduce
lst=[1,2,3,4,5]
#sum=0
#for i in lst:
#    sum=sum+i
sum=reduce(lambda x,y:x+y,lst)
product=reduce(lambda x,y:x*y,lst)
print(sum)
print(product)