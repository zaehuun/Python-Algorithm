def solution(s):
    answer = ''
    
    s = list(s)
    s[0] = s[0].upper()
    print(s)
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    
    return ''.join(s)
