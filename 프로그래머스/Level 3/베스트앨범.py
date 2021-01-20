#https://programmers.co.kr/learn/courses/30/lessons/42579
#하 뭔가 걍 너무 대충 푼 느낌이 강하다.
#좀 더 효율적으로 깔끔하게 처리할 수 있는 방법이 있을까

def solution(genres, plays):
    answer = []
    dic = dict()
    
    for idx, gen in enumerate(genres):
        if gen not in dic:
            dic[gen] = [plays[idx],[[idx,plays[idx]]]]
        else:
            dic[gen][0] += plays[idx]
            dic[gen][1].append([idx,plays[idx]])
    
    li = []
    for i in dic.keys():
        dic[i][1].sort(reverse = True, key=lambda x : x[1])
        li.append((dic[i][0],i))
    li.sort(reverse=True)

    for i in li:
        tmp = i[1]
        if len(dic[tmp][1]) < 2:
            answer.append(dic[tmp][1][0][0])
        else:
            answer.append(dic[tmp][1][0][0])
            answer.append(dic[tmp][1][1][0])

    return answer
