"""
Gabriel Abney
SDEV 220 - Software Development Using Python
Module 2 Lab - Case Study: if...else and while

This application accepts users inputs for name and GPA \
and evaluates if the student qualifies for the Dean's List \
or honor roll. It then prints out this result.
"""

# constants and variables
l_name: str = "" # student last name, will be user input
f_name: str = "" # student first name, will be user input
gpa: float = None # student GPA, will be user input
SENTINEL: str = "ZZZ" # sentinel value to quit program

# main program body loop
while True:
    l_name = input(f"Input the student's last name, or type '{SENTINEL}' to quit: ")
    if l_name.upper() == SENTINEL: # checks if input is sentinel to exit program
        print("Goodbye.")
        break
    else:
        f_name = input("Input student's first name: ")
        gpa = float(input("Input the student's GPA: "))
        match gpa:
            case 