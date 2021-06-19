def solution(record):
    answer = []
    id = dict()
    for r in record:
        m = r.split()
        if m[0] == "Enter":
            id[m[1]] = m[2]
            answer.append((m[1],"님이 들어왔습니다."))
        elif m[0] == "Leave":
            answer.append((m[1],"님이 나갔습니다."))
        elif m[0] == "Change":
            id[m[1]] = m[2]
    #print(answer)
    t = []
    for i in answer:
        t.append(id[i[0]]+i[1])
    return t
