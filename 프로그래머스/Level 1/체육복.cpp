//https://programmers.co.kr/learn/courses/30/lessons/42862

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int lsize = lost.size();
    int rsize = reserve.size();
    
    vector<int> student;
    for(int i = 0; i < n; i++)
        student.push_back(1);
    for(int i = 0; i < lsize; i++)
        student[lost[i]-1]--; //인덱스 -1 하는 게 맞나
    for(int i = 0; i < rsize; i++)
        student[reserve[i]-1]++;
    //이렇게 하면 student에 체육복 없는 학생은 0 여분 있는 학생은 2 자기 거만 있으면 0
    // [2 0 2 0 2 ] -> [1 1 1 1 2]
    
    //양끝은 자기 옆만 체크
    //양끝이아닌 경우 양쪽다체크
    for(int i = 0; i < n; i++){
        if((i == 0) && student[i] == 0){ //제일왼쪽인경우
            if(student[i+1]>1){ //자기 오른쪽이 여벌 체육복있다면
                student[i]++;
                student[i+1]--;
            }
        }
        else if((i == n-1) && student[i] == 0){ //제일오른쪽
            if(student[i-1]>1){ //자기 왼쪽이 여벌 체육복 있다면
                student[i]++;
                student[i-1]--;
            }
        }
        else if(student[i] == 0){ //양끝이아닌경우
            if(student[i-1]>1){
                student[i]++;
                student[i-1]--;
            }
            else if(student[i+1]>1){
                student[i]++;
                student[i+1]--;
            }
        }
    }
    for(int i : student)
        if(i)
            answer++;
    return answer;
}
