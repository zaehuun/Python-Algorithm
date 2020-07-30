//https://programmers.co.kr/learn/courses/30/lessons/42842

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    for(int i = 1; i <= yellow; i++){
        if(yellow % i == 0){
            int col_yellow = yellow / i; //세로 개수
            int row_yellow = yellow / col_yellow; //가로 개수
            
            int col_size = col_yellow + 2;
            int row_size = row_yellow + 2;
            if((col_size * row_size - yellow == brown) && (row_size >= col_size)){
                answer.push_back(row_size);
                answer.push_back(col_size);
            }
        }
    }
    return answer;
}
