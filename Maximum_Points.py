# Solved
t = int(input())
for tt in range(t):
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    result = 0
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if (i * arr[0] + j * arr[1] + k * arr[2]) <= 240:
                    result = max(result, i * brr[0] + j * brr[1] + k * brr[2])
    print(result)