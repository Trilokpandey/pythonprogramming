#f=open("sonu.txt","w")
#f.write("i am a good boy.")

#f=open("sonu.txt","a")
#f.write("his another name is trilok")

#f=open("sonu.txt","r+")
#print(f.read())
#f.write("he is very cool")
#f.close()

with open("sonu.txt") as f:
    print(f.read(4))
    print(f.readlines())
    print(f.readline())#it won't print anything bcz readlines will already read till the end
