//https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    total = []
    for i in skill_trees:
        tmp = []
        for j in i:
            if j in skill:
                tmp.append(j)
        total.append(tmp)

    for a in total:
        c = True
        for i, j in zip(skill, a):
            if i != j:
                c = False
                break
        if c == True:
            answer += 1
    return answer
