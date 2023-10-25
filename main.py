import matplotlib.pyplot as plt
import numpy as np


def plot (a, b, c, point):
    plt.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]])
    plt.plot(point[0], point[1], 'ro') # ro = red circle
    plt.show()


def is_in (a,b,c,point):

    def sign(p1, p2, p3): # it is the cross product 
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    

    d1 = sign(point, a, b)
    d2 = sign(point, b, c)
    d3 = sign(point, c, a)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def rotate_triangle(a,b,c,center = [1,0], angle = 90): # a,b,c and center must be a list of 2 elements [x,y]
    triangle = np.array([[a[0],b[0],c[0]], [a[1],b[1],c[1]]])
    triangle_centered = triangle - np.array([[center[0]], [center[1]]])
    print(triangle)

    angle = np.deg2rad(angle)

    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    triangle = rotation_matrix.dot(triangle_centered) #revisar esto porque esta mal

    print(triangle)



a = [0, 0]
b = [1, 0]
c = [0, 1]

point = [1, 0]

plot(a, b, c, point)

rotate_triangle(a,b,c,point)

print(is_in(a, b, c, point))

if is_in(a, b, c, point):
    print("The point is inside the triangle")
    print("Distance: ", point[0] - a[0])