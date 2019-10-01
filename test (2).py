import math

#let's start with defining the function that asks for input
def get_vertex():
    x = float(input("   Please enter x: "))
    y = float(input("   Please enter y: "))
    return x,y

#for get_triangle we simply need to call get_vertex three times and adding a print to differentiate each one
def get_triangle():
    
    print("First vertex")
    x1,y1 = get_vertex()

    print("Second vertex")
    x2,y2 = get_vertex()

    print("Third vertex")
    x3,y3 = get_vertex()

    return x1, y1, x2, y2, x3, y3
    #this can also be written as return (x1,y1) , (x2,y2) , (x3, y3) to return a tuple (ch. 7.7)

#next we tackle side length. We need the math module in order to use the square root
def side_length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#next we have to calculate the area of the triangle with Heron's formula, this function will need all 3 corners of the triangle
def calculate_area(x1, y1, x2, y2, x3, y3):

    a = side_length(x1, y2, x2, y2)
    b = side_length(x2, y2, x3, y3)
    c = side_length(x3, y3, x1, y1)

    s = (1/2) * (a + b + c)

    return math.sqrt(s*(s-a) * (s-b) * (s-c))

x1, y1, x2, y2, x3, y3 = get_triangle()
area = calculate_area(x1, y1, x2, y2, x3, y3)
print("Area is ", area)