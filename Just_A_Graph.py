t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = arr[i] - i
    arr = set(arr)
    if len(arr) == 1:
        print(n)
    else:
        print(1)