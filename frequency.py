decibel = input("please input a decibel frquency between 40 - 130 : ")

if decibel == 40:
    print "quite room"
elif decibel > 40 and decibel < 70:
    print 'its between Alarm clock and Quite room'
elif decibel < 40:
    print"please enter decibel between 40 - 130"

if decibel == 70:
    print "Alarm clock"
elif decibel > 70 and decibel < 106:
    print 'its between Alarm clock and Gas lawnmover'

if decibel == 106:
    print"Its Gas lawn mover"
elif decibel > 106 and decibel < 130:
    print 'its between Gas lawn mover and Jack hammer'

if decibel == 130:
    print"its Jack hammer"
elif decibel > 130:
    print"please enter decibel between 40 - 130"
