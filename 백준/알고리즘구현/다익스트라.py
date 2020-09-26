import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수
n, m = map(int,input().split())

#시작 노드 번호
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for _ in range(n+1)] #n+1인 이유는 인덱스 번호로 접근 위해

#방문 체크 리스트
visited = [False] * (n+1)

#최단 거리 테이블
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

#방문 x 노드 중 최단 거리 짧은 노드 번호 리턴
def find_smallest():
    min_v = INF
    index = 0 
    for i in range(1, n+1):
        if distance[i] < min_v and not visited[i]:
            min_v = distance[i]
            index = i

    return index

def dijkstra(start):
    #시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #연결된 노드 간 거리

    #시작 노드 제외한 n-1개 노드에 대해
    for i in range(n-1):
        now = find_smallest()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

 
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
