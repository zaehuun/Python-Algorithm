//https://programmers.co.kr/learn/courses/30/lessons/12917
//처음 코드 : algorithm 사용 x, 다음 코드 : algorithm 사용

#include <string>
#include <vector>
using namespace std;

string solution(string s) {
    string answer = "";
    int len = s.length();
    for(int i = 0; i<len; i++){
        for(int j = i + 1; j<len; j++){
            if(s[i] < s[j]){
                char tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
            }
        }
    }
    answer = s;
    return answer;
}
//////////////////////////////////////////////
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp (char a, char b){
    return a > b;
}
string solution(string s) {
    string answer = "";
    sort(s.begin(), s.end(), cmp);
    answer = s;
    return answer;
}
