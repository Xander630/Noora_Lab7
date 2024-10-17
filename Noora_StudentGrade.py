'''
                    Problem Analysis
First is to Ask the user to input their name,section, Prelim grade, Midterm Grade, Final Grade
Second is to Catch the Value error in the grades inputed by the user, it should not be less than 40 and greater than 100 in any grade
Third is to calculate the prelim  grade percentage, midterm grade percentage, final grade percentage and average grade percentage
Fourth is to Convert  the average grade percentage to GPA basing on the LPU Grading System
Fifth is to print the result in a nice format
Finally, End the program



'''



Name = input("Enter Your Name: ")
Section = input("Enter Your Section: ")
Prelim = float(input("Enter Your Prelim Grade: "))
if Prelim < 40 or Prelim > 100:
    print("Error : Prelim Grade is less than 40 or greater than 100")
    exit()

Midterm = float(input("Enter Your Midterm Grade: "))
if  Midterm < 40 or Midterm > 100:
    print("Error:  Midterm Grade is less than 40 or greater than 100")
    exit()


Finals = float(input("Enter Your Finals Grade: "))
if  Finals < 40 or Finals > 100:
    print("Error: Finals Grade is less than 40 or greater than 100")
    exit()

Prelim = 33.33*(Prelim/100)
Midterm = 33.33*(Midterm/100)
Finals = 33.33*(Finals/100)
Average = (Prelim+Midterm+Finals)
Result = round(Average)
print("\nYour Name: "+Name)
print("Your Section: "+Section)


if Result >= 99 and Result <= 100:
    print("Excellent! Your Final GPA is 1.00")
elif Result >= 96 and Result <= 98:
    print("Outstanding! Your Final GPA is 1.25")
elif Result >= 93 and  Result <= 95:
    print("Superior! Your Final GPA is 1.50 ")
elif Result >= 90 and  Result <= 92:
    print("VeryGood! Your Final GPA is 1.50 ")
elif Result >= 87 and  Result <= 89:
    print("Good! Your Final GPA is 2.00 ")
elif Result >= 84 and  Result <= 86:
    print("Satisfactory, Your Final GPA is 2.25 ")
elif Result >= 81 and  Result <= 83:
    print("Fairly Satisfactory, Your Final GPA is 2.50 ")
elif Result >= 78 and  Result <= 80:
    print("Fair, Your Final GPA is 2.75 ")
elif Result >= 75 and  Result <= 77:
    print("You Passed, Your Final GPA is 3.00 ")
elif Result < 75 and  Result >= 40:
    print("Sorry You Failed, Your Final GPA is 5.00 ")
else:
    print("Invalid Grade Your grade should be greater than 40 and less than 100")
