//https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = []
    max_size = len(s)//2
    if len(s) == 1:
        return 1
    else:
        for size in range(1, max_size+1):
            tmp = s[:size]
            cnt = 1
            result = ""
            for a in range(size, len(s), size):
                if tmp == s[a : a + size]:
                    cnt += 1
                else:
                    if cnt == 1:
                        cnt = ""
                    result += str(cnt) + tmp
                    tmp = s[a:a+size]
                    cnt = 1

            if cnt == 1:
                cnt = ""
            result += str(cnt) + tmp
            answer.append(len(result))
    return min(answer)
