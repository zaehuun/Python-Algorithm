//https://programmers.co.kr/learn/courses/30/lessons/17683
//문자열 내에서 문자열 찾으려면 find를 써도 된다

def solution(m, musicinfos):
    answer = ''
    music = [i.split(',') for i in musicinfos]
    
    m=m.replace('C#','c')
    m=m.replace('D#','d')
    m=m.replace('F#','f')
    m=m.replace('G#','g')
    m=m.replace('A#','a')
    aa = []
    for i in music:
        i[3]=i[3].replace('C#','c')
        i[3]=i[3].replace('D#','d')
        i[3]=i[3].replace('F#','f')
        i[3]=i[3].replace('G#','g')
        i[3]=i[3].replace('A#','a')
        #print(i[3])
        shour, smin = i[0].split(':')
        ehour, emin = i[1].split(':')
        runtime = (int(ehour) - int(shour)) * 60 + int(emin) - int(smin)
        #print(runtime)
        a = runtime // len(i[3])
        b = runtime % len(i[3])
        #print(a,b)
        melody = i[3] * a +i[3][:b]
        print(melody)
        
        c = melody.find(m)
        
        if c != -1:
            aa.append([i[2],runtime])
    
    if not aa:
        return '(None)'
    aa.sort(key=lambda x : x[1],reverse=True)
    
    return aa[0][0]
