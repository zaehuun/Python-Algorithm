//https://programmers.co.kr/learn/courses/30/lessons/12910
//algorithm 만든 사람 진짜 칭찬
//예전엔 arr.size() 같은 거 귀찮아서 for문에 다 넣고 돌렸는데 이러면 for문 돌 때마다 함수 호출해서 성능 안 좋아진다고 시스템 프로그래밍 수업 때 배운 게 기억남
//그래서 for문에 넣은 것과 안 넣은 것 차이 비교해보니 넣었을 땐 0.44ms 나오고 안 넣으니 0.38ms 나옴.
//빨라지긴 하네

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    int size = arr.size();
    for(int i = 0; i < size; i++){
        if(arr[i] % divisor == 0)
            answer.push_back(arr[i]);
    }
    if(answer.size() == 0)
        answer.push_back(-1);
    sort(answer.begin(), answer.end());
    return answer;
}
