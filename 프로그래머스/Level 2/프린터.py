//https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
//특강 들어서 그런가 이전에 풀었던 문제들이 왜 시간 초과가 났는지 대충 알 거 같다
//pop()에 인덱스가 들어갈 수 있는 지 처음 알았다
def solution(priorities, location):
    answer = 0
    
    printer = [(i, j) for i, j in enumerate(priorities)]
    
    while True:
        i, j = printer.pop(0)
        
        if any(j < x[1] for x in printer):
            printer.append((i,j))
        else:
            answer += 1
            if i == location:
                break
    
    return answer
