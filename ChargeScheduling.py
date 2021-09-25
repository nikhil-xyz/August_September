t = int(input())
for tt in range(t):
    n = int(input())
    required_charge = list(map(int, input().split()))
    available_time = list(map(int, input().split()))

    arr = []
    for i in range(n):
        if required_charge[i] <= available_time[i]:
            temp = [i+1, required_charge[i], available_time[i]]
            arr.append(temp)

    arr = sorted(arr, key= lambda x: x[2])

    result = []
    if len(arr) != 0:
        passed_time = arr[0][1]
        result = [[arr[0][0], 0, arr[0][1]]]
    for i in range(1, len(arr)):
        if (arr[i][2] - passed_time) >= arr[i][1]:
        # if (arr[i][2] - passed_time) >= arr[i][1]:
            temp = [arr[i][0], passed_time, passed_time + arr[i][1]]
            result.append(temp)
            passed_time += arr[i][1]
    # print(result)

    print(len(result))
    for i in result:
        print(*i)