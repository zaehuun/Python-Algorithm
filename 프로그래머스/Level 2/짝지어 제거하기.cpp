//https://programmers.co.kr/learn/courses/30/lessons/12973

#include <iostream>
#include<string>
#include <stack>
using namespace std;

int solution(string s)
{
    int answer = 0;
    stack<char> st;
    
    for(char c : s){
        if(st.empty()) st.push(c);
        else{
            if(st.top() == c){
                st.pop();
            }
            else
                st.push(c);
        }
    }
    
    if(st.empty())
        answer = 1;
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}
