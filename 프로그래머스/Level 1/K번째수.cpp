//https://programmers.co.kr/learn/courses/30/lessons/42748
//여전히 stl에 익숙해지지 않았음.
//end() : 마지막 원소의 다음 주소 리턴, assign(a,b) : a,b가 정수면 b를 a만큼 할당, 이터레이터면 [a,b) 원소들 할당

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int i = 0; i<commands.size(); i++){
        vector<int> tmp;
        tmp.assign(array.begin() + commands[i][0]-1, array.begin() + commands[i][1]);
        sort(tmp.begin(),tmp.end());
        answer.push_back(tmp[commands[i][2]-1]);
    }
    return answer;
}
