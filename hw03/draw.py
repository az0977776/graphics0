from display import *
from matrix import *
import math

def add_circle( matrix, cx, cy, cz, r, step ):
    t = 0
    while (t<1.001):
        x = r * math.cos(2*math.pi*t)
        y = r * math.sin(2*math.pi*t)
        add_point(matrix,cx+x,cy+y,cz)
        t += step
        x = r * math.cos(2*math.pi*t)
        y = r * math.sin(2*math.pi*t)
        add_point(matrix,cx+x,cy+y,cz)
        
        
def add_curve( matrix, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == "b":
        x = generate_curve_coefs(x0, x3, x1, x2, "b")
        y = generate_curve_coefs(y0, y3, y1, y2, "b")
    else:
        x = generate_curve_coefs(x0, x2, x1, x3, "h")
        y = generate_curve_coefs(y0, y2, y1, y3, "h")
    t = 0
    while t < 1.001:
        x_0 = point_calc(x, t)
        y_0 = point_calc(y, t)
        t += step
        x_1 = point_calc(x, t)
        y__1 = point_calc(y, t)
        add_edge(points, x_0, y_0, 0, x_1, y_1, 0)

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

