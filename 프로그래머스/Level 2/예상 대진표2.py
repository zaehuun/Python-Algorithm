def solution(n,a,b):
    answer = 0
    #1 2 / 3 4 / 5 6 / 7 8 / 9 10 / 11 12 / 13 14 / 15 16 
    #1 2 / 3 4 / 5 6 / 7 8
    #1a 2 / 3 4b
    #1 2
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while True:
        answer += 1
        if abs(a-b) == 1 and (a//2 != b//2):
            return answer
        
        if a | 1:
            a = (a+1)//2
        else:
            a = a//2
        
        if b | 1:
            b = (b+1)//2
        else:
            b = b//2
    return answer
