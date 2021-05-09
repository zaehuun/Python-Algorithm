num = list(map(int,list(input())))

answer = num[0]

for i in range(1,len(num)):
    if num[i] <= 1 or answer <= 1:
        answer = answer + num[i]
    else:
        answer = answer * num[i]
print(answer)
