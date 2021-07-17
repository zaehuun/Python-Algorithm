#플로이드 와샬

def solution(n, results):
    answer = 0
    arr = [[None] * n for _ in range(n)]
    #i에서 k를 갈 수 있으면 k가 갈 수 있는 곳은 i도 갈 수 있음
    for st, end in results:
        arr[st-1][end-1] = True
        arr[end-1][st-1] = False
    
    for k in range(n):
        for win in range(n):
            for j in range(n):
                if arr[win][k] == None:
                    continue
                    
                if arr[win][k] == arr[k][j]:
                    arr[win][j] = arr[win][k]
                    arr[j][win] = not arr[win][k]
    print(arr)            
                    
    for i in range(n):
        if arr[i].count(None) == 1:
            answer+=1
    return answer
