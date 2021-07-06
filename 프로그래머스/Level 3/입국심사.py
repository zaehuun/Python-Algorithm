#문제 읽고 어떤 식으로 풀어야 할 지 감도 없었다.
#그래서 바로 정답 코드 검색하고 공부했다.
#최적의 답을 찾아야 하고, 데이터 수가 많을 때는 이분 탐색을 생각해보자
def solution(n, times):
    answer = 987654321
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left+right)//2
        
        amount = 0
        for t in times:
            amount = amount + mid // t
        if amount >= n:
            right = mid - 1
            answer = mid
        elif amount < n:
            left = mid + 1
    return answer
