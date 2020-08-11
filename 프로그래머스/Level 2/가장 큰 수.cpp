/https://programmers.co.kr/learn/courses/30/lessons/42746

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool tmp(int a, int b){
    string x = to_string(a);
    string y = to_string(b);
    return x + y > y + x;
}

string solution(vector<int> numbers) {
    string answer = "";
    
    int size = numbers.size();
    
    sort(numbers.begin(), numbers.end(), tmp);
    
    int tmp = 0;
    for(int i = 0; i < size; i++)
        tmp += numbers[i];
    if(tmp == 0){
        answer = "0";
    }
    else{
        for(int a : numbers)
            answer += to_string(a);
    }
    return answer;
}
