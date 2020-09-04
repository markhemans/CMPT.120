count = int(input("Size of square: "))

midpoint = int(count/2)

# outer loop
for x in range(count) :

    # inner loop
    for y in range(count) :

        # if a center exists, & the midpoint position has been reached.
        if ( (count%2==1) & (x==y==midpoint) ) :
            print ("o",end=' ')

        # else, if it is not the midpoint...
        else :
            print ("*",end=' ')

    #to create a new line after inner loop ends and outer loop iterates 
    print()
