N, M, K = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

one = a[-1]
two = a[-2]

answer = 0
cnt = 0
for _ in range(M):
    if cnt != K:
        answer += one
        cnt += 1
    else:
        answer += two
        cnt = 0
print(answer)
