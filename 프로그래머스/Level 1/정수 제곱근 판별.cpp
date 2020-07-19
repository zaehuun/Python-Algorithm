//https://programmers.co.kr/learn/courses/30/lessons/12934

#include <string>
#include <vector>
#include <cmath>
using namespace std;

/*long long solution(long long n) {
    long long answer = 0;
    long long tmp = n/2;
    while(tmp > 0){
        if(tmp * tmp == n)
            return (tmp + 1) * (tmp + 1);
        tmp--;
    }
    answer = -1;
    return answer;
}*/

long long solution(long long n) {
    long long answer = 0;
    long long a = sqrt(n);
    if(pow(a,2) == n)
        answer = (a+1) * (a+1);
    else
        answer = -1;
    return answer;
}
