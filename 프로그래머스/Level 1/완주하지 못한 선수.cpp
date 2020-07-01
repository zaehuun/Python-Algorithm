//https://programmers.co.kr/learn/courses/30/lessons/42576
//오랜만에 문제를 푸니 stl 사용법도 기억이 안 났다.
//다시 공부해서 좀 익혀야겠다.
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for(int i = 0; i<participant.size(); i++){
        if(participant[i] != completion[i])
            return participant[i];
    }
}
