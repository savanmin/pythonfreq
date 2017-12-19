bill = False

minute = float(input("Please enter total minutes you have used this month : "))
text = float(input("Please enter total texts you have used this month : "))

base = 15
fee_911 = 0.44

if minute >50:
    base += (minute-50)* 0.25
    print ('you exhausted your monthly plan and your additional charge for mintues are  : %0.2f ') % ((minute-50)* 0.25)
if text  > 50:
    base += (text-50) * 0.15
    print ('you exhausted your monthly plan and your additional charge for texts are : %0.2f  ') % ((text-50) * 0.15)

sub_total = base + fee_911
tax = sub_total * 0.05
totalbill = sub_total + tax

print ('Base                            : %0.2f' % base)
print ('Additional minutes charges      : %0.2f'  % ((minute-50)* 0.25))
print ('Additional text charges         : %0.2f'  % ((text-50) * 0.15))
print ('911 Fee                         : 0.44')
print ('Sub Total                       : %0.2f' % sub_total)
print ('Tax                             : %0.2f' % tax)
print ('Grand Total                     : %0.2f' % totalbill)




