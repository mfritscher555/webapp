pi = 3.14

def area(radius):
    # to handle commas:
    if isinstance(radius, str):
        radius = radius.replace(",", "_")
        radius = float(radius)
    value = pi * radius ** 2
    return value



print(area("3,000"))