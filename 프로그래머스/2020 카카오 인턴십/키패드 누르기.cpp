//https://programmers.co.kr/learn/courses/30/lessons/67256
//맨 첨엔 거리 구할 때 dfs로 구해야 되나 했는데 너무 비효율적이고..
//좌표로 구할까 했는데 하나 하나 다 맵핑 시키는 것이 귀찮았다..
//다른 코드는 금방 작성했는데 31,32번 줄 코드 구하는 데에만 거의 30분 쓴 거 같다


#include <string>
#include <vector>
#include <cmath>
using namespace std;
 
string solution(vector<int> numbers, string hand) {
    string answer = "";
    int size = numbers.size();
    int l_cur_pos = 10;
    int r_cur_pos = 12;
   
    for(int i = 0; i < size; i++){
        if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
            answer += "L";
            l_cur_pos = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
            answer += "R";
            r_cur_pos = numbers[i];
        }
        else{
            if(numbers[i] == 0) numbers[i] = 11; //현재 왼손 4, 오른손 2인 상황에서 5누르면 오른손 잡이라면 오른손이 5를 눌러야 하는데 왼손이 5를 누름, 값을 빼서 절대값 취하는 식을 좀 바꿔야 함
            //
            int l_dist = abs(numbers[i] - l_cur_pos);
            int r_dist = abs(numbers[i] - r_cur_pos);
            l_dist = l_dist / 3 + (l_dist % 3 -1);
            r_dist = r_dist / 3 + (r_dist % 3 -1);
            if(l_dist > r_dist) { //오른손이 더 가까운 경우
                answer += "R";
                r_cur_pos = numbers[i];
            }
            else if( l_dist < r_dist){ //왼손이 더 가까운 경우
                answer += "L";
                l_cur_pos = numbers[i];
            }
            else{ //거리가 가까운 경우
                if(hand == "right"){ //오른손잡이
                    answer += "R";
                    r_cur_pos = numbers[i];
                }
                else{ //왼손잡이
                    answer += "L";
                    l_cur_pos = numbers[i];
                }
            }
        }
    }
    return answer;
}
