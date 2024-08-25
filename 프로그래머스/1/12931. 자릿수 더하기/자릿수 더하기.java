import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String num =Integer.toString(n);
        
        for(char i : num.toCharArray()){
            answer +=  Character.getNumericValue(i);
        }
        return answer;
    }
}