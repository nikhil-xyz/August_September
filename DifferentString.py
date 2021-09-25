# Solved
t = int(input())
for tt in range(t):
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())

    arr = []
    for string in strings:
        temp = int(string, 2)
        arr.append(temp)
    arr.sort()

    j = 0
    flag = False
    for i in range(n):
        if j != arr[i]:
            flag = True
            break
        j += 1

    k = "0"
    if flag:
        k = bin(j)[2:]
    else:
        k = "1" * n

    if len(k) < n:
        temp = "0" * (n - len(k))
        k = temp + k
    print(k)

