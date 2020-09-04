# returns the largest of two parameters

def maxOfTwo(num1,num2):
    if num1>num2:
        return num1
    else :
        return num2

# funcion to find the largest of an infinite amount of arguments

#passes the args tuple to the function
def maxOf(*args):
    #assigns the first value in the args tuple to variable 'biggest'
    biggest = args[0]
    # for a given variable oneArg, compare the biggest value to a passed value
    for oneArg in args:
        biggest = maxOfTwo(biggest,oneArg)
    return biggest

print(maxOf(24,10))
print(maxOf(102,12,4,101))
print(maxOf(6,7,8,9,10))
print(maxOf(-6,7,345,9,-400))
