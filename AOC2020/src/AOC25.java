public class AOC25 extends AOC {
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static long task1() {
		int[] in = intArrInput("inputs/input25.txt"); // read public keys
		long val = 1, key = 1;
		while(in[0] != val) {	//get loop size by iterating until cards public key is reached, iterate doors public key simultaneously
			val = val*7%20201227;
			key = key*in[1]%20201227;
		}
		return key;
	}

	static String task2() {
		return "Merry Christmas :)";	//nothing left to do here :)
	}
}