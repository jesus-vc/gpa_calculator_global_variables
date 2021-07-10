#Name: Jesus Vasquez-Cipriano
#Assignment: Module 5 Assignment
#Created on: January 23, 2020
#Last Edit on: January 23, 2020

#This program calculates the overall GPA, given the course grade and corresponding unit count.
#Course count is also automatically calculated.

#Global variables that accumulate totalPoints(grade*units), total units, and course count.

totalPoints = 0
totalUnits = 0
courseCount = 0

#First, define a function whose goal is: To show the menu option and get the user's menu choice.

def display():
    print("\nWelcome to GPA Calculator, which automates your GPA calculation based on each course grade and unit count you enter.\
\nEach time you enter a new course and its corresponding unit count, you're routed back to this menu.\
\nFrom here, you can enter more grades and units, calculate your GPA thus far, or quit the program.\
\n\nNote: Choosing menu option #2 to show your GPA will result in error UNTIL you input your first grade \
and corresponding course unit count.\n\n1. Enter a new course course grade and that course's unit count.\n2. Show GPA.\n3. Quit.")
    menu_selection = int(input("\nSelect 1, 2, or 3: "))
    if menu_selection == 1 or menu_selection==2 or menu_selection==3:
        return menu_selection
    else:
        return -1

#Second, define a function whose goal is: To calculate if the grade and units provided by a user are legal.

def legal(amount,upperBound,lowerBound):
    if amount >= lowerBound and amount <= upperBound:
        return True
    else:
        return False

#Third, define a main function whose goal is: To call display() and legal().
#display() is called: To show and return the user's menu selection.
#legal() is called: To confirm the grade and units inputted are BOTH legal.

def main():
    #Call display() to determine user's menu selection.
    menu_selection = display()
    #If user selects 1, user inputs grade and units, which are accumulated into global variables if both are legal.
    if menu_selection == 1:
        print("\nLet's get a new course grade and its unit count.")
        #Get user to input: (1) grade and (2) corresponding # of units.
        #Each input is assigned to a variable to pass as parameters/arguments for legal function.
        inputted_grade = int(input("\nEnter a course grade: "))
        inputted_units = int(input("\nEnter that course's unit count: "))
        #Now pass these variables to legal function to determine their legality.
        legal_grade = legal(inputted_grade, 4, 0)
        legal_units = legal(inputted_units, 5, 1)
        #If grade AND units are legal, then accumulate grade*units to a global variable
        #and accumulate the total units to another global variable.
        #Else, display error message and give user another attempt at menu selection by calling main().
        if legal_grade == True and legal_units == True:
            #Given grade and units are legal, accumulate grade*units to a global variable
            #and accumulate the units to another global variable.
            global totalPoints
            totalPoints = totalPoints + (inputted_grade*inputted_units)
            global totalUnits
            totalUnits = totalUnits + inputted_units
            #Also accumulate course counts thus far.
            global courseCount
            courseCount = courseCount + 1
            print("\nYou now can input another grade and unit count, show your current GPA, or quit.\n")
            #Call main() to repeat menu selection.
            main()
        else:
            print("\nError. Either or both your grade and units are not legal. A grade can be between 0 to 4 and units 1 to 5. Try again.\n")
            #Call main() to repeat menu selection.
            main()
            
    #If user selects 2, show current GPA.
    elif menu_selection == 2:
        GPA = totalPoints/totalUnits
        print("\nYour current GPA is", GPA, "based on", courseCount, "number of courses.")
        print("\nYou now can input more grades and units to accumulate your GPA, or just quit.\n")
        #Call main() to repeat menu selection.
        main()
        
    #If user selects 3, show a goodbye statement.
    elif menu_selection == 3:
        print('Goodbye')

    #Menu is displayed again if user does not enter 1, 2, or 3.
    elif menu_selection == -1:
        print("\nError. You must select 1, 2, or 3. Here's the menu again.\n")
        main()
        
#Call and activate main to initiate program
main()
