//https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    
    tmp = [rec.split() for rec in record]
    dic = {}
    
    for i in tmp:
        if i[0] == "Enter":
            dic[i[1]] = i[2]
        elif i[0] == "Change":
            dic[i[1]] = i[2]
            
    for i in tmp:
        if i[0] == "Enter":
            answer.append(dic[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(dic[i[1]] + "님이 나갔습니다.")
        
    return answer
