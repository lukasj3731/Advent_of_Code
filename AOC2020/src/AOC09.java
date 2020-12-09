
public class AOC09 extends AOC{
	
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		println("Task 1: "+firstInvalid(longArrInput("inputs/input09.txt")));
	}
	
	static void task2() {
		long[] in = longArrInput("inputs/input09.txt");
		long invalidNum = firstInvalid(in);
		int min = 0,max=0;
		while(min <= in.length && max <= in.length) {	//as long as min and max are within bbounds
			long sum = 0;
			for(int i=min;i<=max;i++)	//sum numers between min and max
				sum += in[i];
			if(sum == invalidNum) {		//if sum matches number
				long minVal = Long.MAX_VALUE,maxVal = -1;
				for(int i=min;i<=max;i++) {		//find min and maxx within range
					minVal = Math.min(minVal, in[i]);
					maxVal = Math.max(maxVal, in[i]);
				}
				println("Task 2: "+(minVal+maxVal));
				return;
			} 
			max += (sum < invalidNum)?1:0;	//inc max if range too small
			min += (sum < invalidNum)?0:1;	//inc min if range too big
		}
	}

	static long firstInvalid(long[] in) {	//finds first invalid number
		for(int i=25;i<in.length;i++) {		//loop through everything but preamble
			boolean valid = false;
			for(int a=i-25;a<i;a++)
				for(int b=a+1;b<i;b++)
					if(in[a]+in[b]==in[i])	//if 2 sum up, number is valid
						valid = true;
			if(!valid)	//if no 2 sum up, in[i] is the first invalid number
				return in[i];
		}
		return -1;
	}
}