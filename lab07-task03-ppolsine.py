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