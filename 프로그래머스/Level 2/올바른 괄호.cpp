//https://programmers.co.kr/learn/courses/30/lessons/12909

#include<string>
#include <iostream>
#include <stack>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    
    for(char c : s){
        if(c == '(') st.push(c);
        else if(c==')' && st.empty()) return false;
        else if(c==')') st.pop();
    }
    if(!st.empty())
        answer = false;
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}
