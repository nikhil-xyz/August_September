# Solved
t = int(input())
for tt in range(t):
    n = int(input())
    string = "1" + ("0" * (n - 1))
    i = int(string)
    while (i % 9) != 0:
        i += 1
    if ((i - 3) % 2) == 0:
        print(i - 6)
    else:
        print(i - 3)
