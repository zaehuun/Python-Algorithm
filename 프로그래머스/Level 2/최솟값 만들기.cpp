//https://programmers.co.kr/learn/courses/30/lessons/12941

#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool cmp(int a, int b){
    return a > b;
}
int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(), A.end()); 
    sort(B.begin(),B.end(),cmp); 
    //4 2 1
    //4 4 5
    int size = A.size();
    
    for(int i = 0; i < size; i++)
        answer = answer + A[i] * B[i];

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}
