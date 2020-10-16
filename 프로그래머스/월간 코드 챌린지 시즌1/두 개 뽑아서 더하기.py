//https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    length = len(numbers)
    
    for i in range(length-1):
        for j in range(i + 1,length):
            answer.append(numbers[i]+numbers[j])
            
    answer = sorted(list(set(answer)))
    print(answer)
    return answer
