//https://programmers.co.kr/learn/courses/30/lessons/12925?language=cpp#
//부호가 없으면 + 부호가 있는 거라 생각했는데 잘 읽어보니.. + 부호가 올 경우도 있어서 이 경우엔 걍 아무 일 안 하게 함

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int len = s.length() - 1;
    int tmp = 1;
    while(len>0){
        int num = s[len] - '0';
        answer = answer + num * tmp;
        tmp *= 10;
        len--;
    }
    if(s[0] == '-') answer *= -1;
    else if (s[0] == '+'){} //nothing
    else answer = answer + (s[0] - '0') * tmp;
    return answer;
}
