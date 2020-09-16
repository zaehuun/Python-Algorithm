//https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    citations.sort() #0 1 3 5 6
    length = len(citations)
    for i in range(0,citations[-1]+1):
        h = len([True for j in citations if j >= i])
        noth = len([True for j in citations if j < i])
        if h >= i and noth < i:
            answer = i
    print(answer)
    return answer
