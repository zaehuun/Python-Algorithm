https://programmers.co.kr/learn/courses/30/lessons/12982

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
//
int solution(vector<int> d, int budget) {
    int answer = 0;
    int size = d.size();
    //작은 거 많이 넣어야 함
    sort(d.begin(), d.end()); //[1 2 3 4 5 ];
    int sum = 0;

    for(int i = 0; i < size; i++){
        sum += d[i];
        if(sum > budget) break;
        answer++;
    }
    return answer;
}
