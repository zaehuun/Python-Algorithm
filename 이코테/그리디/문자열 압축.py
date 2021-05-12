def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    max_len = len(s) // 2
    for i in range(1,max_len+1): #if max_len = 6 then  1 2 3 4 5 6
        cnt = 1
        prev = ""
        string = ""
        for idx in range(0,len(s)+1,i): #
            if s[idx:idx+i] == prev:
                cnt = cnt + 1
            else:
                if prev != "":
                    if cnt == 1:
                        string = string + prev
                    else:
                        string = string + str(cnt) + prev
                prev = s[idx:idx+i]
                cnt = 1
        last_idx = 0
        if len(s) // i == 0:
            pass
        else:
            last_idx = len(s) - ((len(s) // i) * i)
        if last_idx:
            string = string + s[len(s)-last_idx:]
        answer.append(len(string))
    return min(answer)
