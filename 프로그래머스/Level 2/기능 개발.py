def solution(progresses, speeds):
    answer = []
    day = 1
    idx = 0
    while idx < len(progresses):
        if progresses[idx] + speeds[idx] * day >= 100:
            cnt = 0
            while idx < len(progresses) and progresses[idx] + speeds[idx] * day >= 100:
                cnt = cnt + 1
                idx = idx + 1
            answer.append(cnt)
        else:
            day = day + 1
    return answer
