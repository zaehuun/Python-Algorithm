#예전에 C++로 풀었던 코드와 비교하면 달라진 것은 이번엔 딕셔너리를 사용해서 좌표를 매핑했다는 것이다.
#좌표 매핑하니까 거리 구하기도 더 쉬워진 거 같고.. 코드도 훨씬 더 보기 깔끔해진 거 같은 느낌이 든다.
def solution(numbers, hand):
    answer = ''
    dic = {1 : (0,0), 2 : (0,1), 3 : (0,2), 
           4 : (1,0), 5 : (1,1), 6 : (1,2),
           7 : (2,0), 8 : (2,1), 9 : (2,2), 
                      0 : (3,1)}
    left = (3,0)
    right = (3,2)
    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            left = dic[number]
        elif number in [3,6,9]:
            answer += "R"
            right = dic[number]
        else:
            x, y = dic[number]
            left_d = abs(left[0] - x) + abs(left[1] - y)
            right_d = abs(right[0] - x) + abs(right[1] - y)
            if left_d > right_d:
                right = dic[number]
                answer += "R"
            elif left_d < right_d:
                left = dic[number]
                answer += "L"
            else:
                if hand == "right":
                    right = dic[number]
                    answer += "R"
                else:
                    left = dic[number]
                    answer += "L"

    return answer
