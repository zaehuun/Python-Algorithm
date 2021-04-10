#https://www.acmicpc.net/problem/1018
#아니 체스판 첫 칸 기준으로 안 맞는 칸들 다 바꾸는 거 아니었나
#내가 문제를 이상하게 이해한건가 나는 첫 칸에 따라 다르게 체크 검사했는데 첫 칸 상관 없이 다 검사해야 됐다. 흠...

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

w = ['W','B','W','B','W','B','W','B']
b = ['B','W','B','W','B','W','B','W']

wanswer = []
banswer = []

for i in range(8):
    if i % 2 == 0:
        wanswer.append(w)
        banswer.append(b)
    else:
        wanswer.append(b)
        banswer.append(w)

def check(color,tmp1):
    cnt = 0 
    if color == 'black':
        for i in range(8):
            for j in range(8):
                if tmp1[i][j] != banswer[i][j]:
                    cnt += 1
    else:
        for i in range(8):
            for j in range(8):
                if tmp1[i][j] != wanswer[i][j]:
                    cnt += 1
    return cnt
def arr88(x,y):
    global arr
    tmp = [arr[i][y-8:y] for i in range(x-8,x)]
    return min(check('black',tmp), check('white',tmp))


answer = []

for i in range(N):
    for j in range(M):
        if i + 8 <= N and j + 8 <= M:
            answer.append(arr88(i+8,j+8))
print(min(answer))
