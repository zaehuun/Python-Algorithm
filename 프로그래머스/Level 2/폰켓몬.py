//https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0

    pick = len(nums)//2
    
    nums = list(set(nums))
    
    tmp = 1
    for i in range(0, len(nums)-1):
        if nums[i] < nums[i+1]:
            tmp+=1
            
    if tmp > pick:
        return pick
    else:
        return tmp
        
