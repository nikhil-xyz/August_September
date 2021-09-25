t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    arr.sort()
    brr.sort()

    result = brr[0] - arr[1]
    flag = False
    for i in range(n-1):
        if (brr[i]-arr[i+1]) != result:
            flag = True
            break
    if flag | (result <= 0):
        print(brr[0]-arr[0])
    else:
        print(result)