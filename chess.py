pos = raw_input("Please enter your position : ")

ans = list(pos)

integer = int(ans[1])

abc = {'a':0, 'b':1, 'c':0, 'd':1, 'e':0, 'f':1, 'g':0, "h": 1}

string = abc.get(pos[0])


if integer % 2 == 0:
    print("Column starts with a white square")
    if string==0:
        print("you are in white")
    else:
        print("you are in black")

if integer % 2 != 0:
    print("Column starts with a black square")
    if string==0:
        print("you are in black")
    else:
        print("you are in white")

