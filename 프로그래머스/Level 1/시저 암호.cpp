//https://programmers.co.kr/learn/courses/30/lessons/12926

#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(s[i] == ' '){ //공백일 때
            answer += ' ';
        }
        else if(s[i] >= 'A' && s[i] <= 'Z'){
            if(s[i] + n > 'Z') answer += s[i] + n - 26;
            else answer += s[i] + n;
        }
        else if(s[i] >= 'a' && s[i] <= 'z'){
            if(s[i] + n > 'z') answer += s[i] + n - 26;
            else answer += s[i] + n;
        }        
    }
    return answer;
}
