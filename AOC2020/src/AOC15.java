import java.util.Arrays;

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
		int[] m = new int[limit];	//limit-sized array cause 2 numbers can never be further apart than that. this was a hashmap before, but an array is way faster (and uses less memory according to my testing)
		for(int i=0;i<in.length-1;i++)	//put starting numers into array
			m[in[i]] = i+1;
		int nextNum=in[in.length-1], currNum;	//put last starting number into variable
		for(int i=in.length;i<limit;i++) {	//play game till limit is reached
				nextNum = -m[currNum = nextNum];	
				nextNum += nextNum !=0?i:0;			//get nextNum. if it didn't exist before, it's 0, otherwise i-lastOccurrence
				m[currNum]=i;	//save occurrence to number
		}
		println("Task "+taskNum+": "+nextNum);	//print nextNum after all iterations are done
	}
}