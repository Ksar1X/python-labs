from math import sqrt, pow

a, b, c = int(input("A: ")), int(input("B: ")), int(input("C: "))

d = pow(b, 2) - 4 * c * a

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1, x2)
elif d < 0:
    print("No solutions")
else:
    x = -b/2*a
    print(x)