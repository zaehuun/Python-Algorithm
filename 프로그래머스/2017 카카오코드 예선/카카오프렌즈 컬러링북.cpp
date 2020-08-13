//https://programmers.co.kr/learn/courses/30/lessons/1829
//테케는 통과되는데 채점하면 틀려서 찾아보니 solutuin 함수 내에서 전역변수들 초기화 시켜야 한다는 특이한 조건이 있는 문제...
//dfs로 풀까하다가 퍼져나가는 방식이 bfs가 더 이쁘서 bfs로..
//너무 더럽게 

#include <vector>
#include <queue>

using namespace std;
int dx[4];
int dy[4];
bool visit[100][100];
int mm;
int mn;
int tmp;
vector< vector<int> > k;
void bfs(int a, int b, int v){
    visit[a][b] = true;
    queue< pair<int,int> > que;
    que.push(make_pair(a,b));
    int cnt = 1;
    
    while(!que.empty()){
        int x = que.front().first;
        int y = que.front().second;
        que.pop();
        
        for(int i = 0; i < 4; i++){
            int tx = x + dx[i];
            int ty = y + dy[i];
            
            if(tx < 0 || ty < 0 || tx >= mm || ty >= mn) continue;
            if(!visit[tx][ty] && (k[tx][ty] == v)){
                visit[tx][ty] = true;
                cnt++;
                que.push(make_pair(tx,ty));
            }
        }

    }

    if (tmp < cnt)
        tmp = cnt;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    dx[0] = 1; dx[1] = -1; dx[2] = 0; dx[3] = 0;
    dy[0] = 0; dy[1] = 0; dy[2] = -1; dy[3] = 1;
    for(int i = 0; i < 100; i++)
        for(int j = 0; j < 100; j++)
            visit[i][j] = false;
    tmp = 0;
    k = picture;
    mm = m;
    mn = n;
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(!visit[i][j] && picture[i][j] != 0){
                number_of_area++;
                bfs(i,j,picture[i][j]);
            }
        }
    }
    answer[0] = number_of_area;
    answer[1] = tmp;
    return answer;
}
