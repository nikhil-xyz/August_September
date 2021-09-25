# Solved
from collections import Counter
t = int(input())
for tt in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = Counter(arr)
    equals, operations = 0, 0
    for i in freq.keys():
        if freq[i] > equals:
            equals = freq[i]
            operations = 0

    if x == 0:
        print(equals, operations)
        continue
    for i in freq.keys():
        if (i ^ x) in freq.keys():
            if (freq[i] + freq[i ^ x]) > equals:
                equals = (freq[i] + freq[i ^ x])
                operations = min(freq[i], freq[i ^ x])
            elif (freq[i] + freq[i ^ x]) == equals:
                if operations > min(freq[i], freq[i ^ x]):
                    operations = min(freq[i], freq[i ^ x])
    print(equals, operations)
