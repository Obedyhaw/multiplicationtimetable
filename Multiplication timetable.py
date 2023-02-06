print("-------------------------------------------Welcome to YhawTech Timetable---------------------------------------------------------")
name=input("What is your name?")
ourNum = int(input("Which number do you want the Multiplication timetable for?:"))
ourRange = range(1,13)
for x in ourRange:
    result = ourNum * x
    print(ourNum, " * ",x,"=",result)



