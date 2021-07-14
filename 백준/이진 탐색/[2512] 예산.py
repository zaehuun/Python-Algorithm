N = int(input())
arr = list(map(int,input().split()))
total = int(input())

if total >= sum(arr):
    print(max(arr))
else:
    left = 0
    right = max(arr)
    arr.sort()
    while left<=right:
        mid = (left+right)//2
        
        t = 0
        for i in arr:
            t = t + min(i,mid)

        
        if t > total:
            right = mid - 1
        else:
            left = mid + 1
    print(right)
