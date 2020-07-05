//https://programmers.co.kr/learn/courses/30/lessons/12915
//처음 코드는 sort 사용 x, 다음 코드는 sort 사용

#include <string>
#include <vector>
using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    int size = strings.size();
    for(int i = 0; i < size; i++){
        for(int j = i + 1; j < size; j++){
               if(strings[i][n] > strings[j][n])
                   strings[i].swap(strings[j]);
               else if(strings[i][n] == strings[j][n]){
                   if(strings[i] > strings[j])
                       strings[i].swap(strings[j]);
            }
        }
    }
    answer = strings;
    return answer;
}
//////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////

#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int index;
bool cmp(string a, string b){
    if(a[index] != b[index]) return a[index] < b[index];
    else return a < b;
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    index = n;
    sort(strings.begin(), strings.end(), cmp);
    answer = strings;
    return answer;
}
