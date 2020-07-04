//https://programmers.co.kr/learn/courses/30/lessons/12919

#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    answer += "김서방은 ";
    int size = seoul.size();
    for(int i = 0; i < size; i++){
        if(seoul[i] == "Kim"){
            answer += to_string(i);
            break;
        }  
    }
    answer += "에 있다";
    return answer;
}
