//https://programmers.co.kr/learn/courses/30/lessons/12930

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool odd = true;
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(s[i] == ' ') odd = true;
        else if(odd){
            s[i] = toupper(s[i]);
            odd = false;
        }
        else{
            s[i] = tolower(s[i]);
            odd = true;
        }
    }
    answer = s;
    return answer;
}
