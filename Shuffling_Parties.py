# Solved
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    indexes = []
    for i in range(1, n+1):
        arr[i-1] = arr[i-1] % 2
        indexes.append(i % 2)
    ones = arr.count(1) + indexes.count(1)
    zeroes = arr.count(0) + indexes.count(0)

    print(min(ones, zeroes))
