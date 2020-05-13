def triangleCurve(x, a, b, c):
    if(x < a): 
        return 0
    elif (a <= x & x < b):
        return (x - a) / (b - a)
    elif (b <= x & x <= c):
        return (c - x) / (c - b)
    else:
        return 0

def trapezoidCurve(x, a, b, c, d):
    if(x < a): 
        return 0
    elif (a <= x & x < b):
        return (x - a) / (b - a)
    elif (b <= x & x < c):
        return 1
    elif (c <= x & x < d):
        return (d - x) / (d - c)
    else:
        return 0
