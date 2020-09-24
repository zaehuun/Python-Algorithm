n, m = map(int, input().split())
line = list(map(int,input().split()))
st = 0
end = max(line)

answer = 0
while st <= end:
    mid = (st + end) //2
    total = 0
    for i in line:
        if i > mid:
            total = total + i - mid

    if total == m:
        answer = total
        st = mid + 1
    elif total > m:
        st = mid + 1
    else: #total < m
        end = mid - 1

print(answer)

