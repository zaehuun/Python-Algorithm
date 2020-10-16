//https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    '''
    1 1 0 0
    1 0 0 0
    1 0 0 1
    1 1 1 1
    '''
    answer = []
    def check(arr):
        check_sum = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                check_sum += arr[i][j]
        length = len(arr)
        unit = length // 2
        
        if length == 1 :#더 이상 못 나눌 때
            return [arr[0]]
        elif check_sum == 0: #0으로만 구성
            return [0]
        elif check_sum == len(arr) * len(arr): #1로만 구성
            return [1]
        
        arr1 = [t[:unit] for t in arr[:unit]] 
        arr2 = [t[unit:] for t in arr[:unit]] 
        arr3 = [t[:unit] for t in arr[unit:]] 
        arr4 = [t[unit:] for t in arr[unit:]] 
        result = check(arr1) + check(arr2) + check(arr3) + check(arr4)
        
        return result
    answer = check(arr)
    one_cnt = 0
    zero_cnt = 0
    for i in range(len(answer)):
        if type(answer[i]) == list:
            if answer[i][0] == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
        else:
            if answer[i] == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
    tmp = []
    tmp.append(zero_cnt)
    tmp.append(one_cnt)
    
    return tmp
