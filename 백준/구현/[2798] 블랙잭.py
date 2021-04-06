#https://www.acmicpc.net/problem/2798

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
