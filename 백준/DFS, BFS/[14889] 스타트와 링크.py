#https://www.acmicpc.net/problem/14889

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
check = [False for _ in range(N)]

member = N//2

answer = 987654321

def teamMake(idx,cnt):
    global answer
    linkSum = 0
    bojSum = 0
    if cnt == member:
        for i in range(N):
            for j in range(N):
                if i != j :
                    if check[i] and check[j]:
                        linkSum += arr[i][j]
                    elif not check[i] and not check[j]:
                        bojSum += arr[i][j]
        answer = min(answer, abs(linkSum-bojSum))
    else:
        for i in range(idx,N):
            if not check[i]:
                check[i] = True
                teamMake(i + 1, cnt + 1)
                check[i] = False

teamMake(0,0)
print(answer)
