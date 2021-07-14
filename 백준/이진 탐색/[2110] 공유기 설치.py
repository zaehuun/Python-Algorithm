N, C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
left = 1
right = arr[-1] - arr[0]

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    before = arr[0]
    for i in range(1,N):
        if before + mid <= arr[i]:
            cnt += 1
            before = arr[i]

    if cnt < C:
        right = mid - 1
    else:
        left = mid + 1
print(right)
