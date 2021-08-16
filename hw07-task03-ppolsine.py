#!/usr/bin/python3

# to create the Rectangle class and its constructor and attributes
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    # to create the getters and setters for the attributes
    def get_rectangle(self):
        return self.length,self.width

    def get_area(self):
        area = self.length * self.width
        return area

    # to create a function to return true if the rectangle is square
    def is_square(self):
        if (self.length == self.width):
            return True

    # to overload equivalence to compare the length and width of two rectangles and return true if they are equal
    def __eq__(self, overload):
        if self.length == overload.length and self.width == overload.width:
            print("True")
        else:
            print("False")

# to create rectangle dimensions
abrect = Rectangle(10,10)
cdrect = Rectangle(10,10)
shrect = Rectangle(10,15)

# to create the getters and call the is_square function to print the example output
sh_rect = shrect.get_rectangle()
print(sh_rect)

ab_area = abrect.get_area()
print(ab_area)

cd_rect = cdrect.is_square()
print(cd_rect)

shrect == abrect
abrect == cdrect