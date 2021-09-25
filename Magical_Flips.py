from collections import defaultdict
from math import pow
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    possible = []
    for i in range(n):
        possible.append(-1)

    binary = defaultdict(list)
    for i in range(n):
        temp1 = bin(arr[i])[2:]
        temp2 = bin(brr[i])[2:]
        temp1 = (31 - len(temp1)) * "0" + temp1
        temp2 = (31 - len(temp2)) * "0" + temp2
        binary[i].append(temp1)
        binary[i].append(temp2)

    for i in range(30, -1, -1):
        count = 0
        for j in range(n):
            if possible[j] == -1:
                if (binary[j][0][30-i] == "0") & (binary[j][1][30-i] == "0"):
                    break
                if (binary[j][0][30-i] == "1") | (binary[j][1][30-i] == "1"):
                    count += 1
            elif possible[j] == 1:
                if binary[j][1][30-i] == "1":
                    count += 1
                    continue
                else:
                    break
            else:
                if binary[j][0][30 - i] == "1":
                    count += 1
                    continue
                else:
                    break

        if count == n:
            for j in range(n):
                if (binary[j][0][30-i] == "0") & (binary[j][1][30-i] == "1"):
                    possible[j] = 1
                elif (binary[j][0][30-i] == "1") & (binary[j][1][30-i] == "0"):
                    possible[j] = 0

    count = 0
    result = int(pow(2, 31) - 1)
    for i in range(n):
        if possible[i] == 1:
            count += 1
            result = result & brr[i]
        elif possible[i] == 0:
            result = result & arr[i]

    count_1 = 0
    for i in range(n):
        if possible[i] == -1:
            count_1 += 1
            if (result & arr[i]) >= (result & brr[i]):
                result = result & arr[i]
            else:
                result = result & brr[i]
                count += 1

    if count_1 == n:
        count = 0
    print(result, count)

