# this program gets an input from a user and stores it in 'count'. The midpoint position is the position that comes after
# the mathematical division of an odd numbered plane feild. At this 'midpoint' position, both horizontally and vertically
# a "*" is printed, otherwise blankspace is printed.

count = int(input("What is the plane-field?: "))

#whitespace
print()
#whitespace

midpoint = int(count/2)

# outer loop
for x in range(count) :
    
    #for even numbered squares, break out of first loop and thus, the program with a message.
    if (count%2==0) :
        print("A cross with", count, "rows has no centre.")
        break;
    
    # inner loop
    for y in range(count) :

        # if a center exists, & we are in the middle horizontally or vertically.
        if ((count%2==1) & ((x==midpoint) | (y==midpoint))) :
            print ("x",end=' ')  
    
        # else, print blank space
        else :
            print (" ",end=' ')
    
    #to create a new line after inner loop ends and outer loop iterates 
    print()

#whitespace    
print()
#whitespace
