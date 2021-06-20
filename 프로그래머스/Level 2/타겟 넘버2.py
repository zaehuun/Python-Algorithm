answer = 0

def dfs(total, numbers, idx,target):
    global answer
    if idx == len(numbers):
        if total == target:
            answer = answer + 1
    else:
        dfs(total+numbers[idx],numbers,idx+1,target)
        dfs(total-numbers[idx],numbers,idx+1,target)

def solution(numbers, target):

    arr = [-numbers[0], numbers[0]]
    
    dfs(-numbers[0],numbers,1,target)
    dfs(numbers[0],numbers,1,target)
    
    print(answer)
    return answer
