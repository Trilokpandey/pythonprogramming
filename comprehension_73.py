############comprehension############
'''
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
'''
#lst=[i for i in range(100) if i%3==0]
#print(lst)

########dictionary comprehension#########

dict={i:f"item{i}" for i in range(1,1000) if i%100==0}
print(dict)
print("\n")
dict1={i:f"item{i}" for i in range(5)}
dict2={value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

########set comprehension#########

food={food for food in ["rice","roti","rice","roti"]}
print(type(food))
print(food)

########generator comprehension#########

evens=(i for i in range(100) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())


