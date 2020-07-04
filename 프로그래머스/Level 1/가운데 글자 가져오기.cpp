//https://programmers.co.kr/learn/courses/30/lessons/12903
//else문에서 처음에 아무생각 없이 answer = a + b; 이런 식으로 했다.
//당연히 string 연산 때문에 이어질 거라고 생각했는데 a와 b의 아스키 코드를 더한 문자가 나왔다.
//그래서 따로 더해줌

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    if(s.length() % 2 == 1)
        answer += s[s.length()/2];
    else{
        answer = s[s.length()/2 -1];
        answer += s[s.length()/2];
    }
    return answer;
}
