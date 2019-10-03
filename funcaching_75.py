import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    #it'll take some time
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now running some work")
    some_work(3)
    some_work(2)
    some_work(6)
    some_work(5)
    print("done:calling again")
    some_work(3)
    some_work(13)
    print("called again:")
    some_work(4)
