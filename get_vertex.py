import math

def get_vertex():
    x = float(input("enter x: "))
    y = float(input("enter y: "))
    return x,y

def get_triangle():
    print("First vertex: ")
    x1, y1 = get_vertex()
    print("Second vertex: ")
    x2, y2 = get_vertex()
    print("Third vertex: ")
    x3, y3 = get_vertex()
    return x1, y1, x2, y2, x3, y3

def side_length(x1, y1, x2, y2, x3, y3):
    a = side_length(x1, y1, x2, y2)

