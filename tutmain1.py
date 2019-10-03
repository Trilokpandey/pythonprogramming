def print_name(string):
    return f"this is mr {string}"

def add(num1,num2):
    return num1+num2+10
print("code came from",__name__)
if __name__ == '__main__':
    print(print_name("rahul"))
    output = add(6, 7)
    print(output)

