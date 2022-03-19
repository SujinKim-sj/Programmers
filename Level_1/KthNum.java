package com.pro.lv1;

import java.util.Arrays;

public class KthNum {
	
	public static int[] solution(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];
		
		for(int i = 0; i < commands.length; i++) {
			//start = commands[i][0];
			//end = commands[i][1];
			int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
						
			Arrays.sort(temp);
			answer[i] = temp[commands[i][2] - 1];
			
		}
		
		return answer;
	}

	public static void main(String[] args) {
		// 정렬 Lv1. K번째 수
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		
		for(int i = 0; i < commands.length; i++) {
			System.out.println(solution(array, commands)[i]);
		}
		
	}

}
