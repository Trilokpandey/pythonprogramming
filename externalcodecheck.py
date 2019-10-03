kases = int(input("number"))
for kase in range(kases):
    N = int(input("num\n"))
    result = 1
    for i in range(1, N + 1):
        result = result * i
    print(result)