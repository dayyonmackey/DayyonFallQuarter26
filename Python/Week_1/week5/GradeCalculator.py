numberGrade = int(input("Enter your Grade: "))
if(numberGrade >= 90):
    print("You Got an A, Great Job!")
elif(80 <= numberGrade <=89):
    print("You Got a B, Pretty Good!")
elif(70 <= numberGrade <= 79):
    print("You Got a C, Barely Passed.")
elif(60 <= numberGrade <= 69):
    print("You Got a D, Do Better Next Time.")
elif(numberGrade <= 59):
    print("You Got an F, You Suck.")