#!/usr/bin/python3

class SuperHero:
    _name = "Spiderman"
    _speed = 8
    _strength = 8
    _agility = 9
    def __init__(self,name, speed,strength,agility):
        self._name = name
        self._speed = speed
        self._strength = strength
        self._agility = agility

    def set_speed(self, speed):
        self._speed = speed
        return self._speed

    def stronger(self, tons = 10):
        if tons == 10:
            self._strength += 30
        else:
            self._strength += tons
        return self._strength
    
        def __str__(self):
            return f'{self._name} is my favorite Superheros name'
        
        def __len__(self):
            return f'{self._strength} is the level of Spidermans strength'

        def __eq__(self, newhero):
            if self._name == newhero._name:
                return True
            else :
                    return False

class Mutant(SuperHero):
    def stronger(self, tons = 10):
        if tons < 10:
            tons += 70
            return self._strength
        else:
            return False
    
    def affiliation():
        if self._name == Spiderman:
            return "Avengers"

class Eternal(SuperHero):
    _immortal = True
    _heirarchy = 9

def __init__(self, name, speed, strength, agility, immortal, heirarchy):
    super.__init__(name, speed, strength, agility)
    self._immortal = immortal
    self._heirarchy = heirarchy

def stronger(self, tons = 40):
    if tons == 40:
        self._strength += 10
        return self._strength
    self._strength += (tons +10)
    return self._strength

age_in_millions_of_years = 1

def age_in_millions_of_years(new_years):
    if age_in_millions_of_years + new_years < 1:
        age_in_millions_of_years += new_years
    else:
        print("They are age millionaires")
        return False