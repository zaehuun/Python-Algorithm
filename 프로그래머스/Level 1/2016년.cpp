//https://programmers.co.kr/learn/courses/30/lessons/12901

#include <string>
#include <vector>

using namespace std;
int days[] = {31,29,31,30,31,30,31,31,30,31,30,31};
string day[] = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
string solution(int a, int b) {
    string answer = "";
    int sum_days = 0;
    for(int i = 0; i < a-1; i++)
        sum_days += days[i];
    sum_days += b-1;
    
    answer = day[sum_days%7];
    return answer;
}
