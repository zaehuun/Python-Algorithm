//https://www.acmicpc.net/problem/4949
//종강하고 오랜만에.. 스택 문제를 좋아해서..
dic = {'[' : ']', '(' : ')' }

while True:
    st = []
    tmp = input()

    if len(tmp) == 1 and tmp[0] == '.':
        break

    check = True
    for i in tmp:
        if i == '[' or i == '(':
            st.append(i)

        elif i == ']' or i == ')':
            if  st and dic[st[-1]] == i:
                st.pop()
            else:
                check = False
                break
    if not st and check:
        print("yes")
    else:
        print("no")
