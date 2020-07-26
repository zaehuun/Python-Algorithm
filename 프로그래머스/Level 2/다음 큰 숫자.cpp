//https://programmers.co.kr/learn/courses/30/lessons/12911

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int one_cnt = 0;
    int tmpn = n;
    while(tmpn > 0){
        if(tmpn & 1) one_cnt++;
        tmpn = tmpn >> 1;
    }
    /////////////////////////////
    
    
    while (1){
        n++;
        int tmp = n;
        int tmp_cnt = 0;
        while (tmp > 0){
             if(tmp & 1) tmp_cnt++;
            tmp = tmp >> 1;
        }
        
        if(tmp_cnt == one_cnt){
            answer = n;
            break;
        }
    }

    return answer;
}
