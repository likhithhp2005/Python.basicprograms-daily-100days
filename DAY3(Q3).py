# Using Iterative Subtraction
N = 22
a = 1
h = 0

while N > 0:
    if N - a >= 0:
        N -= a
        a += 1
        h += 1
    else:
        break

print(h)