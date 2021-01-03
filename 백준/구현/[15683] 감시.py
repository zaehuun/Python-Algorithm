#https://www.acmicpc.net/problem/15683
#dfs와 브루트 포스라...
#dfs 코드 구조를 어떻게 짤 지 고민이 되어 구조를 좀 참고 했다.
#dfs 문제는 정말 어려운 거 같다!...
#다른 사람들 코드를 보니 딕셔너리로 미리 방향에 따른 좌표를 설정해서 풀기도 하였는데 개인적으로 나는 별로인 거 같다..

from copy import deepcopy
N, M = map(int, input().split())
result = 987654321

def check(checkmap):
    global N, M, result
    tmp = 0
    for i in range(N):
        tmp = tmp + checkmap[i].count('0')
    result = min(tmp,result)

def draw(dmap, direct, y,x):
    global N, M
    map2 = deepcopy(dmap)
    print(direct)
    for i in direct:
        if i == 'r':
            for j in range(x + 1, M):
                if map2[y][j] == '6':
                    break
                if map2[y][j] == '0':
                    map2[y][j] = '#'
        elif i == 'l':
            for j in range(x - 1, -1, -1):
                if map2[y][j] == '6':
                    break
                if map2[y][j] == '0':
                    map2[y][j] = '#'

        elif i == 'd':
            for j in range(y + 1, N):
                if map2[j][x] == '6':
                    break
                if map2[j][x] == '0':
                    map2[j][x] = '#'

        elif i == 'u':
            for j in range(y - 1, -1, -1):
                if map2[j][x] == '6':
                    break
                if map2[j][x] == '0':
                    map2[j][x] = '#'
    return map2


def dfs(map, idx):
    global cnt, cctv
    if idx >= cnt:
        check(map)
        return
    y, x, cam = cctv[idx]
    if cam == '1':
        new_map = draw(map,['r'],y,x) #오른쪽
        dfs(new_map, idx+1)

        new_map = draw(map,['l'],y,x) #왼쪽
        dfs(new_map, idx+1)

        new_map = draw(map,['u'],y,x) #위
        dfs(new_map, idx+1)

        new_map = draw(map,['d'],y,x) #아래
        dfs(new_map, idx+1)

    elif cam == '2':
        new_map = draw(map,['r','l'],y,x) #왼 오
        dfs(new_map, idx+1)

        new_map = draw(map,['u','d'],y,x) #위 아래
        dfs(new_map, idx+1)

    elif cam == '3':
        new_map = draw(map,['r','u'],y,x) #위 오
        dfs(new_map, idx+1)

        new_map = draw(map,['u','l'],y,x) #위 왼
        dfs(new_map, idx+1)

        new_map = draw(map,['l','d'],y,x) #왼 아래
        dfs(new_map, idx+1)

        new_map = draw(map,['d','r'],y,x) #오 아래
        dfs(new_map, idx+1)

    elif cam == '4':
        new_map = draw(map,['r','u','l'],y,x) #ㅗ
        dfs(new_map, idx+1)

        new_map = draw(map,['u','l', 'd'],y,x) #ㅓ
        dfs(new_map, idx+1)

        new_map = draw(map,['l','d', 'r'],y,x) #ㅜ
        dfs(new_map, idx+1)

        new_map = draw(map,['d','r', 'u'],y,x) #ㅏ
        dfs(new_map, idx+1)

    elif cam == '5':
        new_map = draw(map,['r','u','d','l'],y,x) #+
        dfs(new_map, idx+1)
    #print(map)

arr = [] #전체
cctv = [] #cctv 위치와 값
cnt = 0 #cctv 개수
for i in range(N):
    tmp = input().split()
    arr.append(tmp)
    for j in range(len(tmp)):
        if arr[i][j] != '0' and arr[i][j] != '6':
            cnt += 1
            cctv.append([i,j,arr[i][j]])

dfs(arr,0)
print(result)
'''
[['0', '0', '0', '0', '0', '0'], 
['#', '2', '#', '#', '#', '#'], 
['0', '0', '0', '0', '6', '0'], 
['0', '6', '#', '#', '2', '#'], 
['0', '0', '0', '0', '0', '0'], 
['0', '0', '0', '0', '0', '5']]

[['0', '0', '0', '0', '0', '0'], 
['#', '2', '#', '#', '#', '#'], 
['0', '0', '0', '0', '6', '0'], 
['0', '6', '0', '0', '2', '0'], 
['0', '0', '0', '0', '#', '0'], 
['0', '0', '0', '0', '#', '5']]
[['0', '0', '0', '0', '0', '0'], ['#', '2', '#', '#', '#', '#'], ['0', '0', '0', '0', '6', '0'], ['0', '6', '0', '0', '2', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '5']]
[['0', '#', '0', '0', '0', '0'], ['0', '2', '0', '0', '0', '0'], ['0', '#', '0', '0', '6', '0'], ['0', '6', '#', '#', '2', '#'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '5']]
[['0', '#', '0', '0', '0', '0'], ['0', '2', '0', '0', '0', '0'], ['0', '#', '0', '0', '6', '0'], ['0', '6', '0', '0', '2', '0'], ['0', '0', '0', '0', '#', '0'], ['0', '0', '0', '0', '#', '5']]
[['0', '#', '0', '0', '0', '0'], ['0', '2', '0', '0', '0', '0'], ['0', '#', '0', '0', '6', '0'], ['0', '6', '0', '0', '2', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '5']]
[['0', '0', '0', '0', '0', '0'], ['0', '2', '0', '0', '0', '0'], ['0', '0', '0', '0', '6', '0'], ['0', '6', '0', '0', '2', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '5']]
'''
