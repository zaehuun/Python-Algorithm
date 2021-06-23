def solution(s):
    answer = []
    s = s[2:-2]
    li = s.split('},{')
    li.sort(key=lambda x:len(x))
    for i in range(len(li)):
         li[i] = list(map(int,li[i].split(',')))
    
    dic = dict()
    for i in li:
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    li = sorted(dic.items(), key=lambda x : x[1], reverse=True)

    for i in li:
        answer.append(i[0])
    return answer
