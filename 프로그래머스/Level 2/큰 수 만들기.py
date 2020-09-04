//https://programmers.co.kr/learn/courses/30/lessons/42883#
//999, 2인경우 9를 출력해야되는데 이거에 대해 처리를 안 해서 12번만 계속 실패가 떠서 따로 처리함
def solution(number, k):
    answer = ''
    tmp = []
    #1. combinations는 시간초과 뜸
    #2. tmp에 하나씩넣어가며 비교
    #3. k만큼 tmp에 없을 경우 append
    #4. k개가 있다면 새로 들어온 수를 tmp[-1]과 비교
    #5. top[-1] 보다 작으면 continue, 크면 i보다 큰 수가 있을 때까지 pop
    #6  남은 숫자들과 k 계속 확인 (할 필요 있나? 나중에 끝나고 확인하고 추가하면 될듯)
    for i in number:
        if not tmp:
            tmp.append(i)
        else:
            while tmp and tmp[-1] < i and k > 0:
                k -= 1
                tmp.pop()
            tmp.append(i)

    while k != 0:
        tmp.pop()
        k-=1
    return ''.join(tmp)
