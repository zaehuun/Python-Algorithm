//https://www.acmicpc.net/problem/4673

numbers = [i for i in range(1,10001)]
not_self = []

for i in numbers:
    tmp = i
    for st in str(i):
        tmp += int(st)
    not_self.append(tmp)

not_self = set(not_self)

self_num = []

for i in numbers:
    if i not in not_self:
        self_num.append(i)

self_num.sort()

for i in self_num:
    print(i)

