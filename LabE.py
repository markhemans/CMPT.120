# returns the larges of two parameter
def maxOfTwo(num1,num2):

    # if first parameter is greater than the second, print it
    if num1>num2:
        return num1

    # vice versa
    else :
        if num2>num1:
            return num2


# returns the largest of three parameters from the comparison of the first two   
def maxOfThree(num1,num2,num3):

    #if the result of maxOfTwo is greater than third paramter, return it.
    if (maxOfTwo(num1,num2)) > num3:
        return maxOfTwo(num1,num2)
    # else return the third parameter
    else :
        if (maxOfTwo(num1,num2)) < num3:
            return num3
    


# calls function maxOfTwo, saves it into a result variable, and print it
a = input("Enter first parameter: ")
b = input("Enter second parameter: ")
result = maxOfTwo(a,b)
print("The larger parameter is:",result)

# calls function maxOfThree, saves the returned value into the result variable, and prints it
c = input("Enter a third parameter: ")
result = maxOfThree(a,b,c)
print("The largest parameter is:",result)

# test results
result1 = maxOfTwo(5,7)
print(result1)
result2 = maxOfTwo(105,7)
print(result2)
result3 = maxOfTwo("yes","no")
print(result3)
result4 = maxOfThree(8,16,1)
print(result4)
result5 = maxOfThree(28,16,1)
print(result5)
result6 = maxOfThree(28,16,106)
print(result6)
result7 = maxOfTwo(False,0)
print(result7)
result8 = maxOfTwo(0,False)
print(result8)
result9 = maxOfTwo(0,"")
print(result9)
