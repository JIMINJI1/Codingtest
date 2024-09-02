import java.util.Arrays;

class Solution {
    public long solution(long n) {
       long answer = 0;  

        String str = Long.toString(n); 
        
 
        char[] charArray = str.toCharArray();
        

        Arrays.sort(charArray);
        

        StringBuilder sb = new StringBuilder(new String(charArray));
        

        sb.reverse();
        
        
        answer = Long.parseLong(sb.toString());
        
        return answer; 
    }
    
}