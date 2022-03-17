package com.pro.lv1;

import java.util.HashMap;

public class Marathon {
	public static String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        
        //getOrDefault : 동일한 키가 있으면 participant[i]에 매핑되어있는 값 반환, 아니면 0 반환 
        for(int i = 0; i < participant.length; i++) {
        	//참가자 value에 1
        	map.put(participant[i], map.getOrDefault(participant[i], 0) + 1);
        }
        
        for(int i = 0; i < completion.length; i++) {
        	//완주자 목록에 있으면 해당 완주자 value에 -1
        	map.put(completion[i], map.get(completion[i]) - 1);
        }
        
        //완주하지 못한 참가자는 value가 0이 아닌 값을 가진 참가자이다
        for(int i = 0; i < participant.length; i++) {
        	if(map.get(participant[i]) != 0) {
        		answer = participant[i];
        	}
        }
        return answer;
    }
	public static void main(String[] args) {
		String[] participant = {"leo", "kiki", "eden"};
		String[] completion = {"eden", "kiki"};
		
		System.out.println(solution(participant, completion));	//출력 : leo
	}

}
