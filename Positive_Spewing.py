t = int(input())
from math import ceil
for tt in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if (len(set(arr)) == 1) & (arr[0] == 0):
        print(0)
        continue
    elif k == 0:
        print(sum(arr))
        continue

    count = 0
    i = 0
    brr = {}
    zeroes = []
    while i < n:
        flag = False
        temp = 0
        if arr[i] == 0:
            temp = 1
            flag = True
            j = i + 1
            while j < n:
                if arr[j] == 0:
                    temp += 1
                    j += 1
                else:
                    i = j
                    break
            if j == n:
                i = n
                if (arr[n-1] == 0) & (arr[0] == 0):
                    x = 0
                    while arr[x] == 0:
                        temp += 1
                        x += 1
                    del zeroes[0]
            zeroes.append(temp)
        else:
            carry = 0
            x = i - 1
            if x == -1:
                x = n-1
            y = i + 1
            if y == n:
                y = 0
            if arr[x] != 0:
                carry += 1
            if arr[y] != 0:
                carry += 1
            brr[i] = carry
        if flag is not True:
            i += 1
        count = max(count, temp)

    limit = min(k, ceil(count / 2))

    addition = 0
    for i in brr.keys():
        if brr[i] == 2:
            addition += arr[i] + (limit * 2)
        elif brr[i] == 1:
            addition += arr[i] + (((limit - 1) * 2) + 1)
        else:
            addition += arr[i] + ((limit - 1) * 2)
    for i in zeroes:
        hold = 0
        if (i % 2) == 0:
            hold = min(k, int(ceil(i / 2))) - 1
            addition += ((hold * (hold + 1)) * 2) + 2
            addition += ((limit - hold - 1) * 2 * i) + ((limit - hold - 1) * 4)
        else:
            hold = min(k, int(ceil((i / 2)))) - 1
            addition += ((hold * (hold + 1)) * 2) + 2
            addition += ((limit - hold - 1) * 2 * i)
    addition += ((k - limit) * 2 * n)
    print(addition)
