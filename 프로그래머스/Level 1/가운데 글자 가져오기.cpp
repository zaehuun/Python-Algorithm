//https://programmers.co.kr/learn/courses/30/lessons/12903
//else문에서 처음에 아무생각 없이 answer = a + b; 이런 식으로 했다.
//당연히 string 연산 때문에 이어질 거라고 생각했는데 a와 b의 아스키 코드를 더한 문자가 나왔다.
//그래서 따로 더해줌
//그니까 좀 더 정확히 말하자면 string을 index로 직접 접근하기에 예시로 s = "apple"인 경우, s[0]인 a는 char형임
//이전엔 내가 char + char 했기에 아스키 코드 더한 값으로 계산이 돼서 결과가 이상했었음
//string + string인 경우는 합쳐짐

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
