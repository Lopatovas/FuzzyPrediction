def And(x, y):
    return min(x, y)

def Or(x, y):
    return max(x, y)

def DoubleAnd(x, y, z):
    return And(And(x, y), z)