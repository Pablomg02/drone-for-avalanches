import matplotlib.pyplot as plt


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

a = [15, 0]
b = [50, 40]
c = [50, -40]

point = [40, 20]

plot(a, b, c, point)

print(is_in(a, b, c, point))

if is_in(a, b, c, point):
    print("The point is inside the triangle")
    print("Distance: ", point[0] - a[0])