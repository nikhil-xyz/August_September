# Solved
t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    maximum = max(arr)
    result = 0
    for i in range(n):
        if i >= (k-1):
            if arr[i] == maximum:
                result += (n-i)
    print(result)
