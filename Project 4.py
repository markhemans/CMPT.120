count = int(input("Size of square: "))
for x in range(count) :
    for y in range (count) :
        if (count%2==1) :
            if (x==y) :
                if ((x!=(round(count/2)))&(y!=round(count/2))) :
                    print ("*",end='')
                else : 
                    print("o",end='')
            else :
                print ("*",end='')
        else :
           print ("*",end='') 
    print()

   
