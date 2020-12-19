import java.util.Arrays;

public class AOC13 extends AOC {
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static int task1() {
		String[] in = StringArrInput("inputs/input13.txt");
		int time = pInt(in[0]);
		int[] busses = Arrays.stream(in[1].replaceAll("x,", "").split(",")).mapToInt(AOC::pInt).toArray();
		for (int t = time; t < Integer.MAX_VALUE; t++)
			for (int i = 0; i < busses.length; i++)
					if (t % busses[i] == 0)
						return ((t - time) * busses[i]);
		return -1;
	}

	static long task2() {
		String[] in = StringArrInput("inputs/input13.txt");
		int[] b = Arrays.stream(in[1].replaceAll("x,", "").split(",")).mapToInt(AOC::pInt).toArray();		//extract all numbers into array
		int[] a = new int[b.length];
		for(int i=0;i<b.length;i++)
			a[i] = ((-countChar(in[1].substring(0,in[1].indexOf(""+b[i])),',')%b[i])+b[i])%b[i];	//count index of b and save to a, also making sure a is positive
		return chineseRemainder(b, a);
	}
}