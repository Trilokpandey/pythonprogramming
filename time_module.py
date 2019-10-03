import time
'''
initial=time.time()
print(initial)

k=0
while(k<20):
    print("hello boss,i am coming")
    time.sleep(2) #it'll keep the monitor to sleep for 2 sec
    k+=1
print(f"while loop take {time.time()-initial} second")

initial2=time.time()
for i in range(20):
    print("hello boss,i am going")
print(f"for loop take {time.time()-initial2} second")

'''
local_time=time.asctime(time.localtime(time.time()))
print(local_time)
