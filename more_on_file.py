f=open("pandey.txt")
print(f.tell())
print(f.readline())
print(f.tell())#tells the location of pointer
print(f.readline())
f.seek(10)#set the pointer at specified location
print(f.readline())
f.close()