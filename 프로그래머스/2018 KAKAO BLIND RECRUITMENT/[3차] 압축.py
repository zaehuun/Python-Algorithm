//https://programmers.co.kr/learn/courses/30/lessons/17684
//하 이건 도움을 좀 받았다..
//인덱스 처리를 잘 못 해서 까다로웠다..
//다시 풀어보기
def solution(msg):
    answer = []
    
    alpha = {}
    for i in range(1, 27):
        alpha[chr(64+i)] = i

    st = 0
    
    while st < len(msg):
        tmp = ''
        for i in range(st,len(msg)):
            tmp += msg[i]
            if tmp not in alpha:
                answer.append(alpha[tmp[:-1]])
                st = i
                alpha[tmp] = len(alpha) + 1
                break
        else:
            answer.append(alpha[msg[st:]])

            break

    return answer
