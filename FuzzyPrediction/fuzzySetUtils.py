import numpy as np

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

def trapezoidOutputHelper(x, abcd):
    a, b, c, d = abcd

    y = np.ones(len(x))

    idx = np.nonzero(x <= b)[0]
    y[idx] = triangleOutputHelper(x[idx], [a, b, b])

    idx = np.nonzero(x >= c)[0]
    y[idx] = triangleOutputHelper(x[idx], [c, c, d])

    idx = np.nonzero(x < a)[0]
    y[idx] = np.zeros(len(idx))

    idx = np.nonzero(x > d)[0]
    y[idx] = np.zeros(len(idx))

    return y

def triangleOutputHelper(x, abc):
    a, b, c = abc

    y = np.zeros(len(x))

    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

    idx = np.nonzero(x == b)
    y[idx] = 1
    
    return y

