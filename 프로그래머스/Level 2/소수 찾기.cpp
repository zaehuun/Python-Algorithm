//https://programmers.co.kr/learn/courses/30/lessons/42839
//next_permutation이란 함수는 진짜 좋은 거 같다.. 경우의 수를 다 찾을 수 있네
//unique 함수는 연속으로 중복된 수를 뒤로 보내는 함수라 사용 전에 정렬을 시켜놔야 한다.

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int arr[10000000];
bool cmp(char a, char b){
    return a > b;
}
int solution(string numbers) {
    int answer = 0;
    
    sort(numbers.begin(), numbers.end(), cmp);
    int max_num = stoi(numbers);
    int len = numbers.length();
    for(int i = 2; i <= max_num; i++){
        if(arr[i]) continue;
        for(int j = i + i; j <= max_num; j += i)
            arr[j] = 1;
    }
    
    sort(numbers.begin(), numbers.end());
    
    
    vector<int> vec;
    do{
        string tmp = "";
        for(int i = 0; i < len; i++){
            tmp += numbers[i];
            vec.push_back(stoi(tmp));
        }
    }while(next_permutation(numbers.begin(),numbers.end()));
    
    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(),vec.end()), vec.end());
    
    int size = vec.size();
    
    for(int i = 0; i < size; i++){
        cout<<vec[i]<<endl;
        if(arr[vec[i]] == 0 && vec[i] > 1)
            answer++;
    }
    
    return answer;
}
