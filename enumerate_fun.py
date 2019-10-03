list1=["apple","mango","grape","orange"]
'''
i=1
for item in list1:
    if i%2==0:
        print(f"pandey purchase:{item}")
    i+=1
'''

for index,item in enumerate(list1):
    if index % 2 == 0:
        print(f"pandey purchase:{item}")
