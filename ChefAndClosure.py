from collections import Counter
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = Counter(arr)
    if len(freq) > 3:
        print(0)
        continue

    minus, zero, plus, other = 0, 0, 0, 0
    if -1 in freq.keys():
        minus = freq[-1]

    if 0 in freq.keys():
        zero = freq[0]

    if 1 in freq.keys():
        plus = freq[1]

    other = n - (minus + zero + plus)
    if other > 1:
        print(0)
        continue

    if other == 1:
        if minus > 0:
            print(0)
        else:
            print(1)
    elif minus > 1:
        if plus > 0:
            print(1)
        else:
            print(0)
    else:
        print(1)

