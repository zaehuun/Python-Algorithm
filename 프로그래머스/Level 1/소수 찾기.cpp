//https://programmers.co.kr/learn/courses/30/lessons/12921

//2를 제외한 2의 배수들 체크
//3을 제외한 3의 배수들 체크
//4의 배수들은 2의 배수들에서 체크 됨
//체크 안 된 것들의 배수들을 체크한다.
//결과적으로 체크 안 된 것들이 소수

#include <string>
#include <vector>

using namespace std;
int arr[1000000];
int solution(int n) {
    int answer = 0;
    for(int i = 2; i <= n; i++){
        if (arr[i] == 1) continue;
        for(int j = i << 1; j <= n; j += i)
            arr[j] = 1;
    }
    
    for(int i = 2; i <= n; i++)
        if(arr[i] == 0)
            answer++;
    return answer;
}
