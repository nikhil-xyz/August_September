# Solved
t = int(input())
for tt in range(t):
    n, l, r = map(int, input().split())

    if r > n:
        print(r)
        continue
    if (n > l) & (r > n):
        print(n)
        continue

    result = n
    current_sum = n
    for i in range(r, l - 1, -1):
        addition = 0
        temp = n
        while temp >= i:
            addition += (temp % i)
            temp = int(temp / i)
        addition += temp
        if addition < current_sum:
            current_sum = addition
            result = i
        if current_sum == 1:
            break
    print(result)
