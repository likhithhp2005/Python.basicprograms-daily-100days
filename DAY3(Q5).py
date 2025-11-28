# Using Factor Pairs
num = 12
res = num

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        factor = num // i
        res = min(res, i + factor)

print(res)