//오랜만에 푸는 거라 간단하 거 풀어봤다.
import sys
while True:
    st = sys.stdin.readline().rstrip('\n')

    s = 0
    b = 0
    n = 0
    sp = 0
    if not st:
        break
    for i in range(len(st)):
        if st[i].isdigit():
            n += 1
        elif st[i] == ' ':
            sp += 1
        elif 'a'<= st[i] <= 'z':
            s += 1
        elif 'A' <= st[i] <= 'Z':
            b += 1

    sys.stdout.write("{} {} {} {}\n".format(s,b,n,sp))

