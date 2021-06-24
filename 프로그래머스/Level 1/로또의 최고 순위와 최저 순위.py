def solution(lottos, win_nums):
    answer = []
    correct = 0
    second = 0
    for i in lottos:
        if i in win_nums:
            correct+=1
    if correct == 6:
        second = 1
    elif correct == 5:
        second = 2
    elif correct == 4:
        second = 3
    elif correct == 3:
        second = 4
    elif correct == 2:
        second = 5
    else:
        second = 6
    correct = 0
    first = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
    zero_cnt = lottos.count(0)
    if correct + zero_cnt == 6:
        first = 1
    elif correct + zero_cnt == 5:
        first = 2
    elif correct + zero_cnt == 4:
        first = 3
    elif correct + zero_cnt == 3:
        first = 4
    elif correct + zero_cnt == 2:
        first = 5
    else:
        first = 6
    answer.append(first)
    answer.append(second)
    return answer
