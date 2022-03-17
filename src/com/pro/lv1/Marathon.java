package com.pro.lv1;

import java.util.Arrays;

public class Marathon {
	public static String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Arrays.sort(participant);
        Arrays.sort(completion);
       
        for(int i = 0; i < completion.length; i++) {
        	if(!participant[i].equals(completion[i])) {
        		answer = participant[i];
        	}
        	System.out.println(participant[i]
        			);
        }
        
        return answer;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] participant = {"leo", "kiki", "eden"};
		String[] completion = {"kiki", "eden"};
		
		System.out.println(solution(participant, completion));
	}

}
