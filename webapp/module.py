

# pi is a global variable since it does not change
pi = 3.141592658979


def area(radius):
    radius = float(radius)
    value = pi * radius ** 2
    return value




def circumference(radius):
    radius = float(radius)
    value = 2 * radius * pi
    return value
