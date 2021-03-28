//자바로 풀어보았다..
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        List<Integer> s = new ArrayList<Integer>();
        int idx = 0;
        int day = 1;
        
        int len = progresses.length;
        
        while ( idx < len){
            int cnt = 0;
            for(int i = idx; i < len; i++){
                if (progresses[i] + day * speeds[i] >= 100){
                    cnt++;
                    idx = i+ 1;
                }
                else
                    break;
            }
            if (cnt != 0)
                s.add(cnt);
            day++;
        
        }
        int[] answer = new int[s.size()];

	    for (int i = 0; i < answer.length; i++) {
		    answer[i] = s.get(i);
	    }
        return answer;
    }
}
