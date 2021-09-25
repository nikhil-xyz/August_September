# Fully Solved
from math import ceil
t = int(input())
for tt in range(t):
    n = int(input())

    triplets = 0
    for i in range(1, int(n/2)+1):
        for j in range(2*i, n+1, i):
            if (n % j) < i:
                triplets += int(n / j)
            else:
                triplets += ceil(n / j)
    print(triplets)