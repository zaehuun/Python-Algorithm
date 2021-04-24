#https://www.acmicpc.net/problem/2644

#수정 전 코드
#아무 생각 없이 dfs로 정답 값을 구하도록 했다.
#운 좋게 마지막 dfs의 호출이 hey == end에서 끝난다면 결과는 맞겠지만
#그럴 일은 거의 없을거고 함수의 리턴 값이 없어져서 answer에는 None이 있게 된다.
#bfs로 풀 걸 그랬다.. 분명히 방법은 맞는 거 같은데 계속 틀려서 print만 엄청 찍어봤는데
#눈치채지못하고 계속 이상한 짓만...
#나중에는 그냥 방문 여부를 판단 하기 위한 check 배열에 촌수를 저장하기로 결정하여 해결했다.
n = int(input())
st, end = map(int,input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
check = [0] * (n+1)
print(check)
for i in range(m):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

def dfs(hey, cnt):

    if hey == end:
        print(hey,cnt)
        return cnt
    
    for i in arr[hey]:
        if not check[i]:
            check[i] = 1
            dfs(i, cnt + 1)

        
check[st] = 1
answer =  dfs(st, 0)
if check[end]:
    print(answer)
else:
    print(-1)
    
    
#수정 코드
n = int(input())
st, end = map(int,input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
check = [0] * (n+1)

for i in range(m):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

def dfs(hey, cnt):
    if hey == end:
        return
    for i in arr[hey]:
        if not check[i]:
            check[i] = cnt + 1
            dfs(i, cnt + 1)

dfs(st, 0)
if check[end]:
    print(check[end])
else:
    print(-1)
