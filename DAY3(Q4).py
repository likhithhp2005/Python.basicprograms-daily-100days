# Python Program for Find Minimum Sum of Factors of Number
# Prime Factorization Method

num = 12
res = 0
i = 2

while i * i <= num:
    while num % i == 0:
        res += i
        num //= i
    i += 1

if num > 1:
    res += num

print(res)