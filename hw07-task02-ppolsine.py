#!/usr/bin/python3

# to create the Dog class and its constructor and attributes
class Dog():
    def __init__(self, name, life_expectancy ,size, coat_type, coat_color_pattern):
        self.name = name
        self.life_expectancy = life_expectancy
        self.size = size
        self.coat_type = coat_type
        self.coat_color_pattern = coat_color_pattern

# to create the class objects and set values to their attributes
gr = Dog("Golden Retriever", 12, "large", "medium", "gold")

pg = Dog("Pug", 15, "small", "short","silver fawn")

cg = Dog("Corgi", 13, "small", "fluffy", "tricolor")