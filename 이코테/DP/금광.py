#예전에 집 페인트칠하기 문제였나 그 문제랑 너무 똑같아서 직접 풀기보단 기억력으로 푼 거 같다...
n, m = map(int,input().split())

li = list(map(int,input().split()))

arr = []
tmp = 0
for i in range(n):
    arr.append(li[tmp:tmp+m])
    tmp = tmp + m
    
for i in range(1,m):
    for j in range(n):
        up = mid = down = 0

        if j == 0:
            up = 0
        else:
            up = arr[j-1][i-1]
        
        if j == n -1:
            down = 0
        else:
            down = arr[j+1][i-1]

        mid = arr[j][i-1]

        arr[j][i] = arr[j][i] +  max(up,mid,down)

answer = 0
for i in range(n):
    answer = max(answer, arr[i][m-1])
print(answer)
