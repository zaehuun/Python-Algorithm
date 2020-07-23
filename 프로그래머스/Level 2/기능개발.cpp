//https://programmers.co.kr/learn/courses/30/lessons/42586

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    int size = speeds.size();
    
    int idx = 0;
    int n = 1;
    while(idx != size){
        int count = 0;
        for(int i = idx; i < size; i++){
            if(progresses[i] + speeds[i] * n >= 100){
                count++;
                idx++;
            }
            else break;
        }
        if(count!=0)
            answer.push_back(count);
        n++;
    }
    
    return answer;
}
