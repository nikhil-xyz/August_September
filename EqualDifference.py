# Solved
from collections import Counter
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n <= 2:
        print(0)
        continue
    freq = Counter(arr)
    result = 0
    for i in freq:
        result = max(result, freq[i])
    print(min(n-result, n-2))
