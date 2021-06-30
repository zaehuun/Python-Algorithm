def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    n = len(citations)
    max_v = citations[0]
    for h in range(max_v,-1,-1):
        use = len([u for u in citations if u >= h])
        unuse = len([u for u in citations if u < h])
        if use >= h and unuse < h:
            return h
        
    return answer
