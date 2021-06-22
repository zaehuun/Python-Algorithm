from itertools import combinations
def solution(orders, course):
    answer = []
    order = []
    for i in orders:
        order.append(sorted(list(i)))
    
    for c in course:
        dic = dict()
        for i in order:
            li = list(combinations(i,c))
            for j in li:
                if j not in dic:
                    dic[j] = 1
                else:
                    dic[j] += 1
        max_v = 0
        result = []
        if len(list(dic.values())):
            max_v = max(list(dic.values()))
            print(max_v)
            if max_v >= 2:
                for i in dic.keys():
                    if dic[i] == max_v:
                        answer.append(i)

    result = [''.join(i) for i in answer]
    result.sort()
    return result
