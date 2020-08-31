//https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    answer = 0
    people.sort()
    #1. 크기 순으로 정렬 /해결
    #2. 제일 큰 값과 제일 작은 값을 먼저 태우려고 노력
    #3. 두 값이 limit 이하면 태워서 보내고 pop / i,j 값은 loop 돌 때마다 양 끝에서 시작
    #4. 두 값이 limit 이상이면 j 값 계속 줄이면서 limit 이하인지 체크
    #5. limit 이하가 되면 pop, i == j 가 되면 하나만 보낼 수 있다는 뜻
    #6. 하나만 보내고 pop
    #7. len == 1 이면 걍 pop 하고 끝 / 해결
    #8. 시간 초과 날 거 같은 느낌
    #result. pop은 결국 시간 초과가 났고 걍 인덱스를 이동시키는 방향으로 결정하고 풀었다
    i = 0
    j = len(people) - 1
    while True:
        
        if i == j: #하나 남은 경우
            answer += 1
            break
            
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            answer += 1
        else:
            j -= 1
            answer += 1
                
        if i > j:
            break
        
    return answer
