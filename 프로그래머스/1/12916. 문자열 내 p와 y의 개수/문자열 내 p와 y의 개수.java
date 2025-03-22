class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cntP = 0;
        int cntY = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = Character.toLowerCase(s.charAt(i));
            
            if (c == 'p') {
                cntP++; 
            } else if (c == 'y') { 
                cntY++; 
            }
        }
        
        if (cntP != cntY) {
            answer = false;
        }

        return answer;
    }
}
