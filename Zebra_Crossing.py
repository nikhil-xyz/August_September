# Solved
t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    string = str(input())

    possible = 0

    for i in range(1, n):
        if string[i] != string[i-1]:
            possible += 1

    if k > possible:
        print(-1)
    else:
        for i in range(n-1, -1, -1):
            if (k % 2) & (string[i] != string[0]):
                print(i + 1)
                break
            elif ((k % 2) == 0) & (string[i] == string[0]):
                print(i + 1)
                break
