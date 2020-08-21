//https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):

    pick = len(nums)//2
    
    nums = len(set(nums))
    
    if nums > pick:
        return pick
    else:
        return nums
        
