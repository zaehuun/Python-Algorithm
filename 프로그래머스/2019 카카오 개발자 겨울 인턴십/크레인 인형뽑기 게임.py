//https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    
    blen_row = len(board)

    st = []
    
    for pick in moves:
        for row in range(0, blen_row):
            if board[row][pick-1] != 0:
                if not st:
                    st.append(board[row][pick-1])
                else :
                    if st[-1] == board[row][pick-1] :
                        
                        st.pop()
                        answer += 2
                    else :
                        st.append(board[row][pick-1])   
                board[row][pick-1] = 0
                break
            
    return answer
