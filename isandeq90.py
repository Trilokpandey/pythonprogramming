########## 'is' vs '==': What's The Difference?#######

# == -value equality(two obj has same value)
# is -reference equality(two references refer to the same  objects)
a=[2,3,4]
b=a
print(b==a)
print(b is a)
a[0]=6
print(b==a)
c=a
print(c is a)
print(c is b)



#Task
#a=[2,3,"34"]
#b=[2,3,"34"]
#print(b is a) false dikhayega
