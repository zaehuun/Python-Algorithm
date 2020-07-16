//https://programmers.co.kr/learn/courses/30/lessons/17682

#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int index = 0;
    vector<int> vec;
    int len = dartResult.length();
    for(int i = 0; i < len; i++){
        if(dartResult[i] >= '0' && dartResult[i] <= '9'){ //숫자는 벡터에 저장
           if(dartResult[i+1] == '0') {//점수가 10인 경우
                vec.push_back(10);
                i++;
           }
            else vec.push_back(dartResult[i]-'0'); //점수가 0~9인 경우
            index++;
        }
        else if(dartResult[i] == 'D') vec[index-1] = pow(vec[index-1],2);
        else if(dartResult[i] == 'T') vec[index-1] = pow(vec[index-1],3);
        else if(dartResult[i] == '*'){
            if(index == 1 ) //처음에 나왔을 때
                vec[index-1] = vec[index-1] * 2;
            else{
                vec[index-1] = vec[index-1] * 2;
                vec[index-2] = vec[index-2] * 2;
            }
        }
        else if(dartResult[i] == '#')
            vec[index-1] = (-1)*vec[index-1];
        else {} //S일 땐 계산 필요 x
        
    }
    for(int i = 0; i < index; i++)
        answer += vec[i];
    return answer;
}
