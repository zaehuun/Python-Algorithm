#visit 변수를 전역으로 선언 했는데 그냥 재귀 함수 호출 할 때마다 visit을 넘겨서 해도 될 거 같다.

visit = []
def dfs(idx,computers):
    global visit
    visit[idx] = True
    for i in range(len(computers[idx])):
        if computers[idx][i] == 1 and not visit[i]:
            dfs(i,computers)

def solution(n, computers):
    global visit
    answer = 0
    visit = [False] * n
    
    for idx in range(n):
        if not visit[idx]:
            print(idx)
            dfs(idx,computers)
            answer += 1
    return answer
