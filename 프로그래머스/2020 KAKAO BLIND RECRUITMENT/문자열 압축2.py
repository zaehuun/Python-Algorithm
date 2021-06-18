def solution(s):
    arr = []
    l = len(s) // 2
    if len(s) == 1:
        return 1
    for size in range(1,l+1):
        pre = ""
        cnt = 1
        answer = ""
        for idx in range(0, len(s)+1, size):
            if pre == "": #맨 처음
                pre = s[idx:idx+size]
            else:
                if pre == s[idx:idx+size]: #이전 거와 같을 때
                    cnt = cnt + 1
                else: #이전 거와 다를 때
                    if cnt == 1: #하나만 일 때는 1이므로 숫자 필요 x
                        answer = answer + pre
                    else:
                        answer = answer + str(cnt) + pre
                    pre = s[idx:idx+size]
                    cnt = 1
        last_idx = len(s) % size
        if last_idx:
            answer = answer + s[len(s)-last_idx:]
        arr.append(len(answer)) 
        
    return min(arr)
  
  
  '''
  last_idx = 0
  if len(s) // i == 0:
      pass
  else:
      last_idx = len(s) - ((len(s) // i) * i)
  if last_idx:
      string = string + s[len(s)-last_idx:]
  과거에 풀 땐 마지막 인덱스를 계산하기 위해 위와 같은 방법으로 풀었는데
  size가 4고 길이가 15면 15 - 3(몫) * 4를 해서 나머지 인덱스 수를 구했다.
  근데 생각해보면 걍 나머지 연산을 하면 되는거라 나머지 연산인 %를 사용해서 풀게 되었다.
  훨씬 더 간단하네
  '''
