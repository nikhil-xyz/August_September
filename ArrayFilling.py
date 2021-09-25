# Fully Solved
from math import gcd

def getLcm(a, b):
    temp1 = gcd(a, b)
    return int((a * b) / temp1)

t = int(input())
for tt in range(t):
    n, m = map(int, input().split())

    values = []
    for i in range(m):
        x, y = map(int, input().split())
        temp = [x, y]
        values.append(temp)

    result = 0
    values = sorted(values, key=lambda x: x[0], reverse=True)
    temp_n = n
    lcm = 1
    for i in range(m):
        if temp_n > 0:
            lcm = getLcm(lcm, values[i][1])
            temp = int(n / lcm)
            result += ((temp_n - temp) * values[i][0])
            temp_n = temp
        else:
            break
    print(result)