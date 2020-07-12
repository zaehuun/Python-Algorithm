//https://programmers.co.kr/learn/courses/30/lessons/17681
//2년 전에 이 문제 처음 봤을 때는 이런 거 어떻게 푸나 했는데 지금 보니 어떻게 푸나 싶다
#include <string>
#include <vector>
#include <cmath>
using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;

    for(int i = 0; i < n; i++){
        int tmp = arr1[i] | arr2[i];
        string tmp_st = "";
        int a = pow(2, n-1);
        while(a > 0){
            if(tmp & a) tmp_st += "#";
            else tmp_st += " ";
            a = a>>1;
        }
        answer.push_back(tmp_st);
    }
    return answer;
}
