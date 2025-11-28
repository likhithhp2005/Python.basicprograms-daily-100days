# Using Binary Search
N = 20
low, high = 0, N
h = 0

while low <= high:
    mid = (low + high) // 2
    coins = mid * (mid + 1) // 2

    if coins <= N:
        h = mid
        low = mid + 1
    else:
        high = mid - 1

print(h)