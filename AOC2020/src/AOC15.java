import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class AOC15 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		int[] in = Arrays.stream(StrInput("inputs/input15.txt").split(",")).mapToInt(Integer::parseInt).toArray();
		Map<Integer, Integer> m = new HashMap<Integer, Integer>();
		for(int i=0;i<in.length-1;i++) {
			m.put(in[i], i+1);
		}
		int nextNum=in[in.length-1];
		
		for(int i=in.length;i<2020;i++) {
			
			if(!m.containsKey(nextNum)) {
				int tmp = nextNum;
				nextNum = 0;
				m.put(tmp, i);
			} else {
				int tmp = nextNum;
				nextNum = (i)-m.get(nextNum);
				m.put(tmp, i);
			}
		}
		
		println("Task 1: "+nextNum);
	}
	
	static void task2() {
		int[] in = Arrays.stream(StrInput("inputs/input15.txt").split(",")).mapToInt(Integer::parseInt).toArray();
		Map<Integer, Integer> m = new HashMap<Integer, Integer>();
		for(int i=0;i<in.length-1;i++) {
			m.put(in[i], i+1);
		}
		int nextNum=in[in.length-1];
		
		for(int i=in.length;i<30000000;i++) {
			if(!m.containsKey(nextNum)) {
				int tmp = nextNum;
				nextNum = 0;
				m.put(tmp, i);
			} else {
				int tmp = nextNum;
				nextNum = (i)-m.get(nextNum);
				m.put(tmp, i);
			}
		}
		
		println("Task 1: "+nextNum);
	}
}