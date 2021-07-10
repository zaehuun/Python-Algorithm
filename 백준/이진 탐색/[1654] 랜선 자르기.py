N, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]

left = 1
right = max(arr)

while left<=right:
    mid = (left + right) // 2

    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= K:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
