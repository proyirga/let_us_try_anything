#!/usr/bin/env python3

class Square:
    """Define a square class"""
    
    def __init__(self, height = "0", width = "0"):
        self.height = height
        self.width = width
        
    @property
    def height(self):
        print("Height: ", end="")
        
        return self.__height
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter number for height: ")

    @property
    def width(self):
        print("Width: ", end="")
        
        return self.__width
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter number for width: ")
            
    def getArea(self):
        return int(self.__height) * int(self.__width)
    
def main():
    sq = Square()
    sq.height = input("Enter Height: ")
    sq.width = input("Enter Width: ")
    area = sq.getArea()
    print(area)
    
    
main()