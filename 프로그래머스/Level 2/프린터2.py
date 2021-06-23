from collections import deque
def solution(priorities, location):
    answer = 1
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    while True:
        p = q.popleft()
        t = False
        print(q)
        for i in q:
            if p[0] < i[0]:
                q.append(p)
                t = True
                break
        if t:
            continue
        else:
            if p[1] == location:
                return answer
            answer += 1

    return answer
