//https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

import numpy as np
def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr1[0])
    
    for i in range(row):
        tmp = []
        for j in range(col):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer
