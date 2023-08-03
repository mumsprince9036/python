class Rectangle:
    def rec_area(self , height , width):
        area = height*width
        print("area of rectangle",area)

class square(Rectangle):
    def squ_area(self,side):
        area = side*side
        print("Area of square",area) 

class Traingle(square):
    def tri_area (self , length , breadth): 
        area = 0.5*length*breadth
        print("Area of triangle",area)
obj = Traingle()
obj.rec_area(10,20)
obj.squ_area(12)
obj.tri_area(12,15)