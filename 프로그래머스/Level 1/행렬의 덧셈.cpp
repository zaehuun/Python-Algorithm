//https://programmers.co.kr/learn/courses/30/lessons/12950

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    int size1 = arr1.size();
    int size2 = arr1[0].size();
    for(int i = 0; i < size1; i++){
        for(int j = 0; j < size2; j++){
            arr2[i][j] = arr2[i][j] + arr1[i][j];
        }
    }
    answer = arr2;
    return answer;
}
