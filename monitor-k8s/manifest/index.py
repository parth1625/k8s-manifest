for x in range (5):
    for y in range (4-x):
        print(' ',end='')
    for z in range(1+2*x):
        if(x%2==0):
            print(chr(65+z),end='')
        else:
            print(chr(97+z),end='')
    for y in range (8-2*x):
        print(' ',end='')
    for z in range(1+2*x):
        if(x%2==0):
            print(chr(97+z),end='')
        else:
            print(chr(65+z),end='')
    print()
for x in range (3,-1,-1):
    for y in range (4-x):
        print(' ',end='')
    for z in range(1+2*x):
        if(x%2==0):
            print(chr(65+z),end='')
        else:
            print(chr(97+z),end='')
    for y in range (8-2*x):
        print(' ',end='')
    for z in range(1+2*x):
        if(x%2==0):
            print(chr(97+z),end='')
        else:
            print(chr(65+z),end='')
    print()