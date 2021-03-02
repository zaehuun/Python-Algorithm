#https://programmers.co.kr/learn/courses/30/lessons/72411
#다시 풀어보자

import itertools
from collections import Counter
def solution(orders, course):

    answer = []
    #print(sorted(orders))
    for i in course:
        arr = []
        for j in orders:
            print(sorted(j))
            t = itertools.combinations(sorted(j),i)
            arr += t

        counter = Counter(arr)

        if  len(counter) != 0 and max(counter.values()) != 1:
            answer = answer + [''.join(i) for i in counter if counter[i] == max(counter.values())]
        #print(answer)
    #print(answer)
    print(answer)
    return sorted(answer)
