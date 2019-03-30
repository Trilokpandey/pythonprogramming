number=22

guess=int(input("enter number  :"))

if guess==number:
    print('congrats,you guessed it.')
    print('(but you will not get money)')

elif guess<number:
     print('no,it is little high.')

else:
    print('no,it is little low')

    print('done') 
