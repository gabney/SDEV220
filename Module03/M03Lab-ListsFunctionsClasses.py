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

class Vehicle(): 
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


while True:
    pass