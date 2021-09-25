# Fully Solved
t = int(input())
for tt in range(t):
    n, p, k = map(int, input().split())

    if p == 0:
        print(1)
        continue

    result = 0
    limit = p % k

    if (n % k) != 0:
        result = (int(n / k) + 1) * limit
    else:
        result = int(n / k) * limit

    if (n % k) >= limit:
        result += int((p - limit) / k) + 1
    else:
        result = (n % k) * (int(n / k) + 1)
        result += (limit - (n % k)) * (int(n / k))
        result += int((p - limit) / k) + 1
    print(result)
