numberOfWeeks = 6
linesInBox = 3
charBoxWidth = 10
numberOfDays = 7
dayCount = 1
blanksRequired = 1

for weeks in range(numberOfWeeks) :
    for line in range(linesInBox) :
        for line in range(linesInBox):
            for days in range(numberOfDays) :
                print("|", end="")

                for char in range(charBoxWidth) :
                    print("-", end="")

                
                for blankChar in range(blanksRequired) :
                    print(" ", end="")

            print("|", end="")
            print()
        


