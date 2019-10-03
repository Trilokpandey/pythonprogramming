'''

def findNumber(arr, k):
    for item in arr:
        if k == item:
            print(f"yes {item}")
            break
        else:
            print("no")

    return item


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()

'''
import math
import os
import random
import re
import sys
'''

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    count = 0
    for item in a, b:
        if a[item] > b[item]:


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


a = [18, 13, 17]
b = [16, 13, 17]
acount = 0
bcount = 0
for item1,item2 in a,b:

    if item1 > item2:
        acount+=1
    elif item1 < item2:
        bcount+=1

print(acount,bcount)
'''
'''
import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for item in ar:
        sum+=item
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''

'''
def abc(arr):
    s = 0
    sum1 = 0
    j = len(arr) - 1
    for i in range(0, len(arr)):
        s += arr[i][i]
        sum1 += arr[i][j]
        j -= 1

    diff = abs(sum1-s)

    return diff

if __name__ == '__main__':
    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().rstrip().split())))
    k=abc(arr)
    print(k)


'''



'''
def find(arr):
    pc = 0
    nc = 0
    zc = 0
    l = len(arr)
    for item in range(l):
        if arr[item] > 0:
            pc += 1
        elif arr[item] < 0:
            nc += 1
        else:
            zc += 1

    print("%.6f"%(pc / l))
    print("%.6f"%(nc / l))
    print("%.6f"%(zc / l))

    #xyz.append(ppc)
    #xyz.append(ncc)
    #xyz.append(zcc)

    #return xyz
    #return (str.format('{0:.6f}', xyz))





if __name__ == '__main__':

    arr = [-4, 3, -9 ,0, 4, 1]
    find(arr)

'''
'''
def abc(n):

    for i in range(1,n+1):
            print(" "*(n-i),"#"*i)


    #for i in reversed(range(1,n+1)):
        #print(" "*(n-i),"#"*i)





if __name__ == '__main__':
    n=int(input())
    abc(n)
'''
'''
def miniMaxSum(arr):
    maxvalue = arr[0]
    minvalue = arr[0]
    sum = 0
    sum1 = 0

    for item in range(1,len(arr)):
        if maxvalue < arr[item]:
            maxvalue = arr[item]
    for item in arr:
        sum += item
    sum =sum - maxvalue

    for item in range(1,len(arr)):
        if minvalue > arr[item]:
            minvalue = arr[item]

    for item in arr:
        sum1 +=item
    sum1 = sum1- minvalue

    print(sum,sum1)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
'''
'''
def birthdayCakeCandles(ar):


    count=0
    maxvalue=ar[0]
    for item in range(1, len(ar)):
        if maxvalue <= ar[item]:
            maxvalue = ar[item]
    for item in range(len(ar)):
        if ar[item]==maxvalue:
            count += 1
    return count

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
'''

'''
def timeConversion(s):
    strp=s
    l = len(strp)
    if s[0:2] == '12' and s[l-2] == 'A':
        return '00' + strp[2:l-2]
    elif s[0:2] == '12' and s[l-2] == 'P':
        return s[0:l-2]
    else:
        ext=strp[l-2]
        if ext=='P':
            m=strp[0:(l-2)]
            x=int(m[0:2])+12
            q=str(x)+m[2:(l-1)]
        else:
            q=strp[0:(l-2)]
            
    return q

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result=timeConversion(s)
    print(result)

    #f.write(result + '\n')

    #f.close()

'''
'''
def gradingStudents(grades):
    new_list = []
    for item in grades:
        if (item%5==0) or (item<38):
            new_list.append(item)
        elif (item >= 38) and (item % 5 != 0):
            n = item//5
            #print(n)
            if ((n+1)*5)-item < 3:
                new_list.append((n+1)*5)
            else:
                new_list.append(item)
        else:
            pass

    return new_list




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

'''
'''
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count = 0
    count1 = 0
    for item in apples:
        if item + a >= s:
            count += 1
    print(count)
    for item in oranges:
        if item + b <= t:
            count1 += 1
    print(count1)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

'''
'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count = 0
    count1 = 0
    abc=[]
    xyz=[]
    for item in apples:
        m= item + a
        abc.append(m)
    #print(abc)
    for item in oranges:
        n=item + b
        xyz.append(n)
    #print(xyz)
    for item in abc:
        if item in range(s,t+1):
            count+=1
    print(count)
    for item in xyz:
        if item in range(s,t+1):
            count1+=1
    print(count1)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
'''

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a=x2-x1
    b=v1-v2
    if v2>v1:
        return "NO"
    elif b%v1==0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()






































