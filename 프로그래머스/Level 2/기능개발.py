//https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
//예전에 c++로 푼 적이 있어서 좀 빠르게 푼 거 같다.

def solution(progresses, speeds):
    answer = []
    
    idx = 0
    day = 1
    while(idx < len(progresses)):
        cnt = 0
        for i in range(idx,len(progresses)):
            if progresses[i] + day * speeds[i] >= 100:
                cnt += 1
                idx = i + 1
            else:
                break
        
        if cnt:
            answer.append(cnt)
        day += 1

    return answer
