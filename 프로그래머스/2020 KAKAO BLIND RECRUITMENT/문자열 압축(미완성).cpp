//https://programmers.co.kr/learn/courses/30/lessons/60057

#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string s) {
    int answer = s.length();

    int max = s.length() / 2;
    int size = 1;

    while(size <= max){
        vector<string> v;
        int cnt = 0;
         if (s.length() % size == 0) {
             cnt = s.length() / size;
        }
         else {
            cnt = s.length() / size + 1;
        }
    
        for (int i = 0; i < cnt; i++) {
            v.push_back(s.substr(i * size, size));
         }
        
   
        string tmp = "";
        for(int i = 0; i < cnt; i++){
            int j;
            for(j = i + 1; j < cnt; j++){
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
