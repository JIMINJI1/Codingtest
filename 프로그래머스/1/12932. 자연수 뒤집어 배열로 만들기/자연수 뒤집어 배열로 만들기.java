class Solution {
    public int[] solution(long n) {
        // 1. 자연수를 문자열로 변환
        String str = Long.toString(n);
        
        // 2. 문자열의 길이만큼 배열 생성
        int[] answer = new int[str.length()];
        
        // 3. 문자열의 끝에서부터 각 숫자를 배열에 저장
        for (int i = 0; i < str.length(); i++) {
            answer[i] = str.charAt(str.length() - 1 - i) - '0';
        }
        
        return answer;
    }
}
