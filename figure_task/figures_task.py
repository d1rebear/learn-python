from math import sqrt

a = float(input("enter the side а : "))
b = float(input("enter the side b : "))
c = float(input("enter the side c : "))
r = float(input("enter the radius: "))

p = (a + b + c) / 2
if (a + b) <= c or (b + c) <= a or (c + a) <= b:
    exit(f' Invalid side values, unable to assemble triangle')
R_inscribed = sqrt(((p - a) * (p - b) * (p - c)) / p)
R_circumscribed = (a * b * c) / (4 * sqrt(p * (p - a) * (p - b) * (p - c)))

if r <= R_inscribed:
    print(f'   The circle is completely contained in a triangle, but cannot be described by it')
elif r >= R_circumscribed:
    print(f'   A triangle fits completely within a circle, but cannot be inscribed in it')
else:
    print(f'   The circle does not fit completely into the triangle, and also the triangle does not fit into it')
print(f'   Entered radius value - {r}')
print(f'   Inscribed circle radius - {R_inscribed} ')
print(f'   Circumscribed circle radius - {R_circumscribed}')
