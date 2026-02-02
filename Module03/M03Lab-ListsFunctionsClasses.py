"""
Gabriel Abney
SDEV 220
Module 03 Lab - Case Study: Lists, Functions, and Classes

This program uses the superclass 'Vehicle' and a subclass 'Automobile' \
that inherits attributes from its parent.  The program itself is run and \
prompts the user to input data about the car attributes, then creates an \
instance of 'Vehicle' called 'car'.  Finally, it prints the attributes \
of the created car to console.
"""

#the Vehicle class
class Vehicle(): 
    def __init__(self, type):
        self.type = type


# the Automobile class, which is a subclass of Vehicle
class Automobile(Vehicle):
    #constructor to build class 
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type) #inherited from Vehicle 
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    # class method to print details abour object attributes
    def attributes(self):
        print(f"Your vehicle's description is:\n\
              Vehicle type: {self.type}\n\
              Year: {self.year}\n\
              Make: {self.make}\n\
              Model: {self.model}\n\
              Number of doors: {self.doors}\n\
              Type of roof: {self.roof}")


#gathers user input to generate attributes for the object
type = input("Please enter the vehicle type (e.g. car, truck, plane): ")
year = input("Please enter the vehicle year: ")
make = input("Please enter the vehicle make: ")
model = input("Please enter the vehicle model: ")
doors = input("Please enter the vehicle's number of doors: ")
roof = input("Please enter the vehicle roof type: ")

# creates the object from user inputs
user_auto = Automobile(type, year, make, model, doors, roof)

# calls the attributes method of the Automobile class to print the object's attribute info
user_auto.attributes()