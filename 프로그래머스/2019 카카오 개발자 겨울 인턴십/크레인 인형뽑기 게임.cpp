//https://programmers.co.kr/learn/courses/30/lessons/64061

//1. 스택이 빈 경우
//2. 뽑은 인형이 스택 top과 같은 경우
//3. 뽑은 인형이 스택 top과 다른 경우
//4. 뽑을 인형이 없는 경우

#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int move_count = moves.size();
    int col_size = board.size();
    int cnt = 0;
    stack<int> st;
    for(int i = 0; i < move_count; i++){
        for(int j = 0; j < col_size; j++){
            if(board[j][moves[i]-1] != 0){
                if(st.empty()){
                    st.push(board[j][moves[i]-1]);
                    board[j][moves[i]-1] = 0;
                    
                }
                else{
                    if (st.top() == board[j][moves[i]-1]){
                        board[j][moves[i]-1] = 0;
                        st.pop();
                        cnt += 2;
                    }
                    else{
                        st.push(board[j][moves[i]-1]);
                        board[j][moves[i]-1]= 0;
                    }
                }
                break;
            }
        }
    }
    return cnt;
}
