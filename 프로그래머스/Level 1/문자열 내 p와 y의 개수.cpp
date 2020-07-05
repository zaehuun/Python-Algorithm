//https://programmers.co.kr/learn/courses/30/lessons/12916
//나는 이런 게 재밌네
//사실 gap 변수는 넣지 않고 'P' 'Y'로 해도 되지만 뭔가 이게 더 재밌음
#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int gap = 'a' - 'A';
    int len = s.length();
    int pcnt = 0;
    int ycnt = 0;
    for(int i = 0; i < len; i++){
        if(s[i] == 'p' || s[i] == ('p' - gap) ){
            pcnt++;
        }
        if(s[i] == 'y' || s[i] == ('y' - gap) ){
            ycnt++;
        }
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;
    if(((ycnt == 0) && (pcnt == 0)) || (ycnt == pcnt) )
        answer = true;
    else if (ycnt != pcnt)
        answer = false;
    return answer;
}
