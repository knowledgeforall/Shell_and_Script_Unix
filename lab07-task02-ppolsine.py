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