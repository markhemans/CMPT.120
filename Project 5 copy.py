numberOfWeeks = 6
linesInBox = 3
charBoxWidth = 10
numberOfDays = 7
dayCount = 1

startCalendarDay = int(input("What day should the calender start on? "))
numberOfDaysInMonth = int(input("How many days are there in this month? "))

for weeks in range(numberOfWeeks):
    for days in range(numberOfDays):
        print( "|", end="")
        for char in range(charBoxWidth):
            print( "-", end="")
    print("|", end="")
    print()

    for line in range(linesInBox):
        for days in range(numberOfDays):
            print("|", end="")
            boxNumber = (weeks*numberOfDays) + days
            blanksRequired = charBoxWidth
            if line == 0:
                 if  (boxNumber >= startCalendarDay) and (dayCount <= numberOfDaysInMonth):
                    print(dayCount, end="")
                    if (dayCount< 10):
                        blanksRequired = blanksRequired - 1
                    else:
                        blanksRequired = blanksRequired - 2
                    dayCount = dayCount + 1
        
            for blankChar in range(blanksRequired):
                print(" ", end="")
        print("|", end="")
        print()

for days in range(numberOfDays):
    print( "|", end="")
    for char in range(charBoxWidth):
        print( "-", end="")
print("|", end="" )
print()
