# Solved
t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    for i in range(k):
        if arr[i] < 0:
            arr[i] = int(abs(arr[i]))
    result = 0
    for i in arr:
        if i <= 0:
            continue
        result += i
    print(result)