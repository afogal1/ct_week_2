from math import pi
def squareFeet(length,width):
    area = length * width
    print(f"{length} ft x {width} ft = {area} sq.ft.")

def circumf(dia):
    circum = round(dia * pi)
    print(f"Circumference of {dia} in. diameter = {circum} in.")