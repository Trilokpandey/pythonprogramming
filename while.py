number=23
running=True

while running:
    guess=int(input('enter number'))

    if guess== number :
              print("congrats")
              running=False
    elif guess<number:
              print('no,number is greter')
    else:
                print('no,it is little lower than that')
else:
        print('the loop is over')

print('done')
