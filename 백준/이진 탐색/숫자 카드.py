N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
answer = []
for num in arr2:
    flag = True
    left = 0
    right = N - 1
    while left<=right:
        mid = (left+right) // 2

        if arr1[mid] == num:
            answer.append(1)
            flag = False
            break
        
        if arr1[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    if flag:
        answer.append(0)
print(' '.join(map(str,answer)))
