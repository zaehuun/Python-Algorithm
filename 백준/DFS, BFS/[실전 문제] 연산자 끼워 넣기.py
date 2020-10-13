n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -123456789
min_value = 123456789

def sol(i, data):
    global add, sub, mul, div, max_value, min_value
    if i == n:
        max_value = max(max_value,data)
        min_value = min(min_value,data)
    else:
        if add > 0:
            add -= 1
            sol(i+1, data+ num[i])
            add += 1
        if sub > 0:
            sub -= 1
            sol(i+1, data - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            sol(i+1, data * num[i])
            mul += 1
        if div > 0:
            div -= 1
            sol(i+1, int(data / num[i]))
            div += 1
sol(1,num[0])
print(max_value, min_value)
