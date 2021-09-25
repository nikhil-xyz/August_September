# Solved
t = int(input())
for tt in range(t):
    n, m, x, y = map(int, input().split())
    diagonal = min(n, m) - 1
    result = min(2 * diagonal * x, diagonal * y)
    remain = max(n, m) - min(n, m)

    if x <= y:
        result += remain * x
    else:
        if (remain % 2) == 0:
            result += remain * y
        else:
            result += ((remain - 1) * y) + x
    print(result)