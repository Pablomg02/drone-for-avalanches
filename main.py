import matplotlib.pyplot as plt
import numpy as np


def plot (a, b, c, point, drone):
    plt.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]])
    plt.plot(point[0], point[1], 'ro') # ro = red circle
    plt.plot(drone[0], drone[1], 'bo') # bo = blue circle
    plt.axis("equal")
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




def rotate_triangle(a,b,c,center = [0,0], angle=0): # a,b,c and center must be a list of 2 elements [x,y]
    triangle = np.array([[a[0],b[0],c[0]], [a[1],b[1],c[1]]])
    triangle_centered = triangle - np.array([[center[0], center[0], center[0]], [center[1], center[1], center[1]]])
    print(triangle)

    angle = np.deg2rad(angle)

    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    triangle_centered = rotation_matrix.dot(triangle_centered) #revisar esto porque esta mal
    triangle = triangle_centered + np.array([[center[0], center[0], center[0]], [center[1], center[1], center[1]]])

    return([triangle[0][0], triangle[1][0]], [triangle[0][1], triangle[1][1]], [triangle[0][2], triangle[1][2]])


"""def rotate_velocity(velocity, angle = 30):
    angle = np.deg2rad(angle)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return rotation_matrix.dot(velocity)"""






point = [0,0]
drone = [3, 2]
angle = 90

a = [drone[0], drone[1]]
b = [drone[0]+1, drone[1]+0.5]
c = [drone[0]+1, drone[1]-0.5]

#plot(a, b, c, point, drone)

a_, b_, c_ = rotate_triangle(a,b,c,drone, angle)

#plot(a_, b_, c_, point, drone)

plt.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]])
plt.plot([a_[0], b_[0], c_[0], a_[0]], [a_[1], b_[1], c_[1], a_[1]])

plt.plot(point[0], point[1], 'ro') # ro = red circle
plt.plot(drone[0], drone[1], 'bo') # bo = blue circle
plt.show()


print(is_in(a, b, c, point))



"""
if is_in(a, b, c, point):
    print("The point is inside the triangle")
    print("Distance: ", point[0] - a[0])
"""