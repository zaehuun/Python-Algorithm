N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
check = list(map(int,input().split()))

for i in check:
    flag = True
    left = 0
    right = N - 1
    while left <= right:
        mid = (right+left) // 2
        if arr[mid] == i:
            flag = False
            print(1)
            break
        if arr[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    if flag:
        print(0)
