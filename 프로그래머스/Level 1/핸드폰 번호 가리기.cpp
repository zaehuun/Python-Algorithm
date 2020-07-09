//https://programmers.co.kr/learn/courses/30/lessons/12948

#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    int len = phone_number.length();
    for(int i = len-1-4; i>=0; i--)
        phone_number[i] = '*';
    answer = phone_number;
    return answer;
}
