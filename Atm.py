print ('Welcome to My ATM \n')

balance = 0
pin = 0
chance = 3

pin = int(input('Please enter your pin : '))


def startAtm(balance):
    while True:


        print  ('Press 1 for balance \n')
        print  ('Press 2 for withdraw \n')
        print  ('Press 3 for deposit \n')

        option = int(input('What would you like to do today ?   :'))
        dummy = 'dummy'
        if type(dummy) == type(option):
            # do something
            print("Do Something...")
        if option == 1:
            print('Your balance is %0.2f' % balance)



        elif option == 2:
            print('Your balance is %0.2f' % balance)
            withdraw = (float(input('How much would you like to withdraw today ?  :')))
            if withdraw > balance or withdraw < 0:
                print('\nInsufficient balance or Invalid input\n'
                      'Please try again\n\n')
            else:
                balance= balance-withdraw
                print('Your balance after last withdrawal is %0.2f' % balance)


        elif option == 3:
            deposit = float(input('How much would you like to deposit today ?  :'))
            balance = balance + deposit
            print('Your updated balance is %0.2f' % balance)


        else:
            print('Please enter valid input')


        print('Press (Y) to continue and (N) to exit \n')
        ask = str(input('would you like to continue ? '))
        if ask != "Y":
            break



while True:
    if pin == 1234 or pin == 1111:
        startAtm(balance)
        break
    else:
        chance = chance - 1
        if chance == 0:
            break
        print('\nPlease try again \n'
              'You have got %d chances left' % chance)
        pin = int(input('Please enter your pin : '))


print("\nThank you for banking with us, \n"
      "You have a good one ahead ! ")

