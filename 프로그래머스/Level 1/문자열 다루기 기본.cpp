//https://programmers.co.kr/learn/courses/30/lessons/12918
//자바나 파이썬에서만 사용했는데 c++에도 있는 지 처음 알았다 
//Ranged-based for loops

#include <string>
#include <vector>
using namespace std;

bool solution(string s) {
    bool answer = true;
    if(s.length() ==4 || s.length() == 6){
        for(char c : s){
            if(c<'0' || c>'9')
                return false;
        }
    }
    else return false;
    return answer;
}
