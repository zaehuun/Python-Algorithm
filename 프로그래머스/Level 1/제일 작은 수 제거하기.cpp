//https://programmers.co.kr/learn/courses/30/lessons/12935

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int min = arr[0];
    int size = arr.size();
    if(size == 1){ answer.push_back(-1);}
    else {for(int i = 1; i < size; i++){
        if(min > arr[i] )
            min = arr[i];
    }
    for(int i = 0; i < size; i++){
        if(arr[i] != min)
            answer.push_back(arr[i]);
    }
         }
    return answer;
}
