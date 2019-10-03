#recursive method
'''
def fact_recursive(n):
    if n==1:
        return 1
    else:
        return n* fact_recursive(n-1)

print("enter the number for factorial")
num=int(input())

print("factorial of",num ,"is :",fact_recursive(num))
'''

#iterative method
'''
def fact_iterative(num):
    fact=1
    i=1
    while(i<=num):
       fact=fact*i
       i=i+1
    return fact

print("enter the number for factorial")
num=int(input())

print("factorial of",num ,"is :",fact_iterative(num))
'''

#fibonaci series by recursive method
#0 1 1 2 3 5

def fibo_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)

print("enter the number for fibonaci series")
num=int(input())

print("fibonaci of",num ,"is :",fibo_recursive(num))