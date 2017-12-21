from random import randint

guess = randint(1,20)
while True:

    userguess = (int(input('Please guess a number from 1 to 20 : ')))
    if userguess < guess:
        print('Go higher')
    elif userguess > guess:
        print('Go lower')
    else:
        print('Well guessed !!!')
        break




