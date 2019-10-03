##########coroutine#####

import time
def searching():
    #some task is taking 4 second
    book="this is a book written by pandey"
    time.sleep(4)

    while True:
        text=(yield )
        if text in book:
            print("text is in book")
        else:
            print("text is not in book")

search=searching()
print("searching will start from here...")
next(search)
print("next method run")
search.send("pandey")
input("press any key")
search.send("written by")
search.close()#after this no code will run
#search.send("this is")
