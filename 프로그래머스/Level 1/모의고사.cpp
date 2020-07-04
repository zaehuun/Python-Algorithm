//https://programmers.co.kr/learn/courses/30/lessons/42840
//어떻게든 깔끔하고 효과적으로 풀려고만 생각하니까 오히려 더 안 풀리는 느낌이었다.
//도저히 안 떠올라서 걍 하나 하나 다 비교하는 법으로 풀었는데 정답이네..
//복잡하게 생각하는 습관을 좀 버려야겠다. 제일 쉬운 방법이 정답인 것이 당연한 소리니


#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> supo1 = {1,2,3,4,5};
    vector<int> supo2 = {2,1,2,3,2,4,2,5};
    vector<int> supo3 = {3,3,1,1,2,2,4,4,5,5};
    int cnt1, cnt2, cnt3;
    cnt1 = cnt2 = cnt3 = 0;
    for(int i = 0; i<answers.size(); i++){
        if(answers[i] == supo1[i%5]) cnt1++;
        if(answers[i] == supo2[i%8]) cnt2++;
        if(answers[i] == supo3[i%10]) cnt3++;   
    }
    int max =  (cnt1>cnt2) ? ((cnt1 > cnt3) ? cnt1 : cnt3) : ((cnt2 > cnt3) ? cnt2 : cnt3);
    if(max == cnt1) answer.push_back(1);
    if(max == cnt2) answer.push_back(2);
    if(max == cnt3) answer.push_back(3);
    sort(answer.begin(), answer.end());
    return answer;
}
