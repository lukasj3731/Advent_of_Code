import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class AOC15 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		task(2020,1);
	}
	
	static void task2() {
		task(30000000,2);
	}
	
	static void task(int limit, int taskNum) {
		int[] in = Arrays.stream(StrInput("inputs/input15.txt").split(",")).mapToInt(Integer::parseInt).toArray();	//input to int array
		Map<Integer, Integer> m = new HashMap<Integer, Integer>();	//map containing [number -> last occurrence]
		for(int i=0;i<in.length-1;i++)	//put starting numers into map
			m.put(in[i], i+1);
		int nextNum=in[in.length-1], currNum;	//put last starting number into variable
		for(int i=in.length;i<limit;i++) {	//play game till limit is reached
				nextNum = i-m.getOrDefault(currNum = nextNum, i);	//if value has occurred before -> (i-last occurence), else -> 0
				m.put(currNum, i);	//save occurence of current number
		}
		println("Task "+taskNum+": "+nextNum);	//print nexxtNum after all iterations are done
	}
}