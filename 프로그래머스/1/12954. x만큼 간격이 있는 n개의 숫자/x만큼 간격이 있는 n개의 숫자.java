class Solution {
    public long[] solution(int x, int n) {
        //크기가 n인 long 타입 배열을 생성
        long[] answer = new long[n]; 
        //열에 넣을 값의 초기값을 x로 설정
        long val = x;
        for (int i = 0; i < n; i++) { //i가 0부터 n-1까지 반복
            //현재 값을 배열의 i번째 위치에 저장
            answer[i] = val;
            //다음에 저장할 값을 x만큼 증가
            val += x;
        }
        //결과 배열을 반환
        return answer;
    }
}
