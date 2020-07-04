//https://programmers.co.kr/learn/courses/30/lessons/12906
//레벨 1 문제지만 4분컷 하니 뭔가 기분 좋다
//마지막에 hello cpp는 왜 넣은거지

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int size = arr.size();
    answer.push_back(arr[0]);
    for(int i = 1; i < size; i++){
        if(arr[i-1] != arr[i])
            answer.push_back(arr[i]);
    }
    cout << "Hello Cpp" << endl;

    return answer;
}
