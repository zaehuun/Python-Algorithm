//https://programmers.co.kr/learn/courses/30/lessons/12947

#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int tmp = 0;
    int store = x;
    while(x > 0){
        tmp = tmp + x % 10;
        x /= 10;
    }
    if(store % tmp != 0) answer = false;
    return answer;
}
