a = input("first number is: ")
b = input("second number is: ")

#exception block
try:
    c = float(a)
    d = float(b)
    answer = (c/d)
    print(c, "/", d, "=", answer)
except:
    print("Your answer did not compute")
