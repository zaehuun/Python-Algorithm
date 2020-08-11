//https://programmers.co.kr/learn/courses/30/lessons/60057

#include <string>
#include <vector>
using namespace std;

int solution(string s) {
    int answer = s.length();

    int max = s.length() / 2;
    int size = 1;

    int len = s.length();
    
    while(size <= max){
        vector<string> v;
        int cnt = 0;
         
    
       for(int i = 0; i < len; i+=size)
            v.push_back(s.substr(i, size));


        string tmp = "";
        int vsize = v.size();
        for(int i = 0; i < vsize; i++){
            int j;
            for(j = i + 1; j < vsize; j++){
                if(v[i] != v[j])
                    break;
            }
            
            if(j == i + 1)
                tmp += v[i];
            else{
                tmp = tmp + to_string(j-i) + v[i];
                i = j - 1;
            }
            
        }
        
        if (tmp.length() < answer)
            answer = tmp.length();
       
        size++;
    }
    return answer;
}
