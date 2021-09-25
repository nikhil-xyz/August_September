# Solved
t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    arr = list(str(input()))

    count = 0
    for i in range(n):
        if arr[i] == '0':
            continue
        if (i + k) < n:
            if arr[i + k] == '1':
                continue
        if (i - k) >= 0:
            if arr[i - k] == '1':
                continue
        if (i + k) < n:
            arr[i + k] = '1'
        else:
            arr[i] = '0'
        count += 1

    print(count)