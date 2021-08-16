#!/usr/bin/python3

# to create the Car class and its constructor and attributes
class Car:
    def __init__(self,wheels,doors,fuel,temperature):
        self.wheels = wheels
        self.doors = doors
        self.fuel = fuel
        self.temperature = temperature

    # to create the getters and setters for the attributes
    def get_wheels(self):
        return self.wheels
    
    def get_doors(self):
        return self.doors

    def get_fuel(self):
        return self.fuel

    def get_temperature(self):
        return self.temperature
    # to be able to change fuel attribute
    def set_fuel(self, fuel):
        self.fuel = fuel
# to create the class object and set values to its attributes
toyota_rav4 = Car(4,5,50,72)

# to redefine variables with getters and setters
wheels = toyota_rav4.get_wheels()

doors = toyota_rav4.get_doors()

toyota_rav4.set_fuel(100)

fuel = toyota_rav4.get_fuel()

temperature = toyota_rav4.get_temperature()

# to print an example output
print(wheels)
print(doors)
print(fuel)
print(temperature)