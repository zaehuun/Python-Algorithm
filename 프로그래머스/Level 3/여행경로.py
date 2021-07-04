#풀면서도 이게 맞는 방법인가 하면서 풀었는데 풀고난 후 다른 코드를 보니 신기하게 푸는 거 보고 좀 감탄..
def dfs(start,route,li,n):
    if len(li) == n + 1:
        return li
    if start in route:
        print(start,route[start],li)
        for r in range(len(route[start])):
            if route[start][r] != "000":
                end = route[start][r]
                li.append(end)
                route[start][r] = "000"
                result = dfs(end,route,li,n)
                if result:
                    return result
                li.pop()
                route[start][r] = end
def solution(tickets):
    answer = []
    
    route = dict()
    for st, end in tickets:
        if st in route:
            route[st].append(end)
        else:
            route[st] = [end]
    n = 0
    for r in route:
        n += len(route[r])
        route[r].sort()
    li = dfs("ICN",route,["ICN"],n)
    return li
