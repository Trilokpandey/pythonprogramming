
f1=open("sonu.txt")

try:
    f2=open("sonu.txt")

except EOFError as e:
    print("eof error occured",e)

except IOError as e:
    print("ioerror occurred",e)

else:
    print("it will run only if except will not execute")
finally:
    print("this will execute anyway whether anything run or not")
    f1.close()
    f2.close()

