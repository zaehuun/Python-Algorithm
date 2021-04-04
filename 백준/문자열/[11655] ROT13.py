#https://www.acmicpc.net/problem/11655
S = input()
answer = ""
for i in S:
    if i == ' ' or '0'<= i <= '9': 
        answer += i
        continue
    
    if 'A' <= i <= 'Z': #대문자
        c = chr(ord(i) + 13)
        if c > 'Z':
            c = ord(c) - ord('Z') + ord('A') - 1
            answer = answer + chr(c)
        else:
            answer += c

    elif 'a' <= i <= 'z': #소문자
        c = chr(ord(i) + 13)
        if c > 'z':
            c = ord(c) - ord('z') + ord('a') - 1 
            answer = answer + chr(c)
        else:
            answer += c

print(answer)
