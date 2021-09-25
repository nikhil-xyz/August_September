#Solved
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if len(set(arr)) == 1:
        print(1)
        continue

    i = n-1
    result = 0
    current_max = arr[n-1]
    flag = False
    while i >= 0:
        j = i-1
        if j == -1:
            break
        while arr[j] <= arr[i]:
            j -= 1
            if j == -1:
                if arr[0] == arr[i]:
                    flag = False
                else:
                    flag = True
                break
        if flag:
            break
        else:
            result += 1
            i = j
    if flag:
        print(-1)
    else:
        print(result)
