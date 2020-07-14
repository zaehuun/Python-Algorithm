//https://programmers.co.kr/learn/courses/30/lessons/42889
//아무생각없이 1.0/2.0이 아니라 1/2가 0.5라는 숫자를 나오기를 기대하며 계속 돌렸다..
//도저히 모르겠어서 비쥬얼 스튜디오에서 결과를 확인해보니 다 0으로 나오는 거 보고 실수형으로 바꿔서 계산하니 통과

#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int count1[501];
int nclear[501];

bool cmp(pair<int, float> a, pair<int,float> b){
    if(a.second == b.second) return a.first < b.first;
    else return a.second > b.second;
}
vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    
    int size = stages.size();
    for(int i : stages){
        nclear[i]++; //스테이지에 도달했지만 성공하지 못한 플레이어 수
       for(int j = 1; j <= i; j++)
           count1[j]++; //스테이지에 도달한 플레이어 수, 제한사항 5도 해결
    }
    
    vector< pair<int, float> > result;
    for(int i = 1; i <= N; i++){
        if(count1[i] == 0) result.push_back(make_pair(i, 0));
        else result.push_back(make_pair(i, (double)nclear[i]/count1[i]));
    }
    
    sort(result.begin(), result.end(), cmp);
    for(int i = 0; i < result.size(); i++)
        answer.push_back(result[i].first);
    return answer;
}
