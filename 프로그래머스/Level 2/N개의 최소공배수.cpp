//https://programmers.co.kr/learn/courses/30/lessons/12953

#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b){
	int c;
	while (b != 0){
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int lcm(int a, int b){
    return a * b / gcd(a, b);
}

int solution(vector<int> arr) {
    int answer = 0;
    
    int size = arr.size();
    answer = arr[0];
    for(int i = 1; i < size ; i++){
        answer = lcm(answer,arr[i]);
    }
    return answer;
}
