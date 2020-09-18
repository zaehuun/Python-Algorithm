n = input()
row = int(n[1])
col = ord(n[0]) - 96

mv = [(-2,-1), (-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(-1,2),(1,2)]
answer = 0
for i in mv:
    trow = row + i[0]
    tcol = col + i[1]

    if trow >= 1 and trow <= 8 and tcol >= 1 and tcol <= 8:
        answer+=1

print(answer)
