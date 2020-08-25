//https://programmers.co.kr/learn/courses/30/lessons/42888
//문제가 길면 안 푸는 습관이 있었는데 그럼 너무 실력이 안늘까봐 걍 참고 읽어봤다.

def solution(record):
    answer = []
    tmp = [i.split() for i in record ]
    

    dict = {id[1] : id[2] for id in tmp if len(id) == 3}

    
    for rec in tmp:
        if rec[0] == "Enter":
            answer.append(dict[rec[1]]+"님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(dict[rec[1]]+"님이 나갔습니다.")
    return answer
