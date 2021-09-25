t = int(input())
for tt in range(t):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    i = n-1
    result = 0
    for j in range(k):
        if (arr[i] + arr[i-1]) >= x:
            result += x
            i -= 2
        else:
            break

    while i >= 0:
        result += arr[i]
        i -= 1
    print(result)
