#define a class
class Bike:
    name = ""
    gear = 0
#create object of class
bike1 = Bike()

# access atributes and assign new values
bike1.gear = 11
bike1.name = "mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear}")