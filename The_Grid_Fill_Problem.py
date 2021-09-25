# Solved
t = int(input())
for tt in range(t):
    n = int(input())
    if n == 2:
        for i in range(2):
            for j in range(2):
                # if i == j:
                print(-1, end=" ")
            print("")
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(-1, end=" ")
                else:
                    print(1, end=" ")
            print("")
