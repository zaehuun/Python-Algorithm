//https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        tmp = 0
        for j in range(i + 1, len(prices)):
            tmp += 1
            if prices[i] > prices[j]:
                break
        answer.append(tmp)
        
    return answer
