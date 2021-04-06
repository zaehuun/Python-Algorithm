#https://www.acmicpc.net/problem/2798
#브루트 포스인 경우 보통 입력 값의 크기가 많지 않은 거 같다.
#이번 경우에도 n이 최대 100이다.

N, M = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0
minusMin = 987654321
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            v = arr[i] + arr[j] + arr[k]
            if v <= M:
                if minusMin > M - v:
                    minusMin = M - v
                    answer = v
print(answer)
