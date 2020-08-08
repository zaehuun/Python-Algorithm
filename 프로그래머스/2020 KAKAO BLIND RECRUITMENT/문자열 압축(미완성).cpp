//https://programmers.co.kr/learn/courses/30/lessons/60057

#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

int solution(string s) {
    int answer = 0;
    int len = s.length();
    int max = len / 2;
    int size = 1;
    answer = len;
    while(size <= max){

        vector<string> vec;
        string tmp = "";
        
        for(int i = 0; i < len; i+=size){
            string tmp = s.substr(i, size);
            //cout<<tmp<<endl;
            vec.push_back(tmp);
        }
        
        int vsize = vec.size();
        
        for(int i = 0; i < vsize; i++){
            
            int j = i + 1;
            ///////////////
            if(vec[i] == vec[j]){
                while(vec[i]!=vec[j]){
                    j++;
                }
            }
            //////////////////
            else{
                tmp += vec[i];
            }
            
            
        }
       
        
        //cout<<tlen<<endl;
        if(tlen < answer)
            answer = tlen;
        size++;
    }
    return answer;
}
