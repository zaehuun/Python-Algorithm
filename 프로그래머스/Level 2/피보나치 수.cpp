//https://programmers.co.kr/learn/courses/30/lessons/12945

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> fib;
    fib.push_back(0);
    fib.push_back(1);
    for(int i = 2; i <= n; i++)
        fib.push_back((fib[i-1] + fib[i-2])%1234567);
    
    answer = fib[n];
    return answer;
}
