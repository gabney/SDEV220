"""
Gabriel Abney
SDEV 220 - Software Development Using Python
Module 2 Lab - Case Study: if...else and while

This application accepts users inputs for name and GPA \
and evaluates if the student qualifies for the Dean's List \
or honor roll. It then prints out this result and begins \
again until the user exits using the sentinel value.
"""

# constants and variables
l_name: str = "" # student last name, will be user input
f_name: str = "" # student first name, will be user input
gpa: float = None # student GPA, will be user input
SENTINEL: str = "ZZZ" # sentinel value to quit program

# main program body loop
while True:
    l_name = input(f"Input the student's last name, or type '{SENTINEL}' to quit: ")
    if l_name.upper() == SENTINEL: # checks if input is sentinel and exits if yes, otherwise continue down
        print("Goodbye.")
        break
    f_name = input("Input student's first name: ")
    gpa = float(input("Input the student's GPA: "))
    if gpa >= 3.5:
        print(f"{f_name} {l_name} has made the Dean's list, congratulations!")
    elif gpa >= 3.25:
        print(f"{f_name} {l_name} has made the Honor Roll, congratulations!")
    else:
        print(f"{f_name} {l_name} did not make any awards.")


    