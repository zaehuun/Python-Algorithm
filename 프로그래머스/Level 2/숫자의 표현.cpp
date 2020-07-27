//https://programmers.co.kr/learn/courses/30/lessons/12924
//동적 문제인 줄 알았는데 규칙도 없는 거 같아서 그냥 풀었다

#include <string>
#include <vector>

using namespace std;
/*
    1 -> 1
    2 -> 2 (1)
    3 -> 1 2, 3 (2)
    4 -> 4 (1)
    5 -> 2 3, 5 (2)
    6 -> 1 2 3, 6 (2)
    7 -> 3 4, 7 (2)
    8 -> 8 (1)
    
*/
int solution(int n) {
    int answer = 0;
    for(int i = 1; i <= n; i++){
        int sum = 0;
        for(int j = i; j <= n; j++){
            sum += j;
            if(sum >= n)
                break;
        }
        if(sum == n)
            answer++;
    }
    return answer;
}
