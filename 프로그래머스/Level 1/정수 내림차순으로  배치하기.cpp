//https://programmers.co.kr/learn/courses/30/lessons/12933

#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(int a, int b){
    return a < b;
}
long long solution(long long n) {
    long long answer = 0;
    
    vector<int> vec;
    while(n>0){
        vec.push_back(n%10);
        n/=10;
    }
    sort(vec.begin(), vec.end(),cmp);
    int tmp = 1;
    for(int i = 0; i < vec.size(); i++){
        answer = answer + vec[i] * tmp;
        tmp *= 10;
    }
    return answer;
}
