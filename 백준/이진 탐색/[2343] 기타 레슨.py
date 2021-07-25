N, M = map(int,input().split())
arr = list(map(int,input().split()))
left = max(arr)
right = sum(arr)
answer = -987654321
while left <= right:
    mid = (left+right) // 2

    tmp_sum = 0
    tmp_cnt = 0
    for i in arr:
        tmp_sum += i
        if tmp_sum + i> mid:
            tmp_cnt += 1
            tmp_sum = 0
        tmp_sum += i
    if tmp_sum:
        tmp_cnt+=1
    # print(tmp_cnt)
    if tmp_cnt > M:
        left = mid + 1
    
    else:
        right = mid - 1

print(left)
    
