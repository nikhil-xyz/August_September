t = int(input())
for tt in range(t):
    n, s = map(int, input().split())
    total_sum = int((n * (n + 1)) / 2)

    temp = total_sum - s
    # print(total_sum, temp)
    if (temp >= 1) & (temp <= n):
        print(temp)
    else:
        print(-1)
