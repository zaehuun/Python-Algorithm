//https://programmers.co.kr/learn/courses/30/lessons/42626
//특강에서 배움
//sort가 nlogn이라 1,000,000개의 데이터가 들어오면 시간초과 뜸
//그래서 한 번 sort로 풀음

def solution(scov, K):
    answer = 0
     
    while True:
        
        scov.sort() #nlogn

        minv = scov.pop(0) #n
        
        if minv >= K: #1
            break
        if not scov: #1
            answer = -1 #1
            break
        
        minv2 = scov.pop(0) #n
        scov.append(minv + minv2 * 2) #1
        answer += 1 #1
    return answer
    
    ##################################################################
    //당연히 시간초과 뜸
    
import heapq

def solution(scov, K):
    answer = 0
    heapq.heapify(scov) #n
    
    while True:
        min1 = heapq.heappop(scov) #logn
        if min1 >= K : #1
            return answer
        if not scov:
            return -1
        
        min2 = heapq.heappop(scov) #logn
        heapq.heappush(scov,min1 + min2 * 2) #logn
        answer += 1
        
