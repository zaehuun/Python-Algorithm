//https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    
    root = [numbers[0],-numbers[0]]
    
    for i in range(1, len(numbers)):
        tmp = []
        for j in root:
            tmp.append(j + numbers[i])
            tmp.append(j - numbers[i])
        root = tmp
        
        
    answer = root.count(target)
    return answer
