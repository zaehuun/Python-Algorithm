def solution(n, results):
    answer = 0
    wins = {}
    loses = {}
    for i in range(1,n+1):
        wins[i], loses[i] = set(), set()
    for win, lose in results:
        wins[win].add(lose)
        loses[lose].add(win)
        
    for i in range(1, n+1): 
        # print(loses)
        for winner in loses[i]: 
            wins[winner].update(wins[i]) 
        for loser in wins[i]: 
            loses[loser].update(loses[i])
        # print(loses)
    print(wins)
    print(loses)
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    # for i in range(1,n+1):
    #     for j in loses[i]:
    #         if i not in wins[j]:
    #             wins[j].append(i)
    #     for j in wins[i]: #j는 진 선수
    #         print(i,loses[j])
    #         if i not in loses[j]: #j가 졌던 선수들 목록에 i가 없으면 i 추가
    #             loses[j].append(i)

    return answer
