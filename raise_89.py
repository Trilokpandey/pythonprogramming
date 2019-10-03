##########raise ###########

# a=input("enter your name:\n")
# b=input("how much do you earn ")
#
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("numbers are not allowed")
#
# print("hello",a)

#1000 lines taking an hour

c=input("enter your name")
try:
    print(a)

except Exception as e:
    if c=="sonu":
        raise ValueError("sonu is not allowed")

    print("exception handled")

#Task
# ImportError - jab interpreter ko koi imported module nhi milta hai tab ye Exception raise hota hai.
# IndentationError - jab kisi program me kahi incorrect indentation hota hai to ye Exception raise hota hai.
# assert(condition) - jab condition false ho to exception raise hogi
# KeyError - when key is not found in dictionary.
# 1.MemoryError: It comes when some command or operation run out of memory or exceeds memory limit.
# EOFError:-jab input function file ka end ma chala jata ha
# NameError: jab variable define na kiya Gaya ho
# FileNotFoundError----yh error tb aata hai jb aap koi aise file ko open kr rhe ho jo ki.. Nhi hai aapke folder me.
# Overflow : jab kisi arithmetic operation ki value bohot zyada badi a rhi ho ki represent na kar paen
# Runtime:jab koi error kisi particular category mein na a paye
# OSError: jab koi operating system related problem aati hai.
# PermissionError: jab koi chij ko open or file ko edit karne ke liye permission nahi hota
