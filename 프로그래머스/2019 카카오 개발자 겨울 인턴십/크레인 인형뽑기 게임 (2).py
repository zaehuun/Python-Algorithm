def solution(board, moves):
    answer = 0
    row = len(board)
    st = []
    for move in moves:
        tmp = 0
        while tmp < row:
            if board[tmp][move-1] != 0:
                if not st:
                    st.append(board[tmp][move-1])
                else:
                    if st[-1] == board[tmp][move-1]:
                        st.pop()
                        answer+=2
                    else:
                        st.append(board[tmp][move-1])
                board[tmp][move-1] = 0
                break
            tmp += 1
                

    
    return answer
