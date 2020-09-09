//https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

def solution(dartResult):
    answer = 0
    point = []
    ten = False
    for idx in range(len(dartResult)):
        i = dartResult[idx]
        if ten:
            ten = False
            continue
        if i.isdigit():
            if int(i) == 1 and dartResult[idx+1] == '0':
                point.append(10)
                ten = True
            else:
                point.append(int(i))
        else:
            if i == 'S':
                continue
            elif i == 'D':
                point[-1] = point[-1]**2
            elif i == 'T':
                point[-1] = point[-1]**3
            elif i == '*':
                if len(point) > 1:
                    point[-2] = point[-2] * 2
                point[-1] = point[-1] * 2
            elif i == '#':
                point[-1] = -1 * point[-1]

    return sum(point)
