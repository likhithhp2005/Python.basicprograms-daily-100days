# Using Matrix Representation
a, b = 35, 15
x, y, u, v = 0, 1, 1, 0

while a != 0:
    q, r = divmod(b, a)
    b, a = a, r
    x, u = u - q * x, x
    y, v = v - q * y, y

print("GCD is", b)
print("x =", u, ", y =", v)