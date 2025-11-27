# Python Program for Extended Euclidean Algorithms
# Using Iterative Extended Euclidean Algorithm
a, b = 35, 15
x0, x1, y0, y1 = 1, 0, 0, 1

while b:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1

print("GCD is", a)
print("x =", x0, ", y =", y0)