#프로그래머스에서 3단계 난이도로 풀었던 문제와 비슷한 문제였다.
N, M = map(int,input().split())
#N 나무 수, M 필요 나무 길이
arr = list(map(int,input().split()))
left = 1
right = max(arr)
answer = 0
def result(arr,mid):
    s = 0
    for i in arr:
        if i > mid:
            s += i - mid
    return s
while left<=right:
    mid = (left+ right) // 2

    s = result(arr,mid) #적정 크기
    if s >= M:
        answer = mid
        left = mid + 1
    elif s < M:
        right = mid - 1
print(answer)

