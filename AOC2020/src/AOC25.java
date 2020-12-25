public class AOC25 extends AOC {
	public static void main(String[] args) {
		 println("Task 1: "+task1());
		 println("Task 2: "+task2());
	}

	static long task1() {
		int[] in = intArrInput("inputs/input25.txt"); // read public keys
		long loop,val = 1;
		for(loop = 0;in[0] != val;loop++)	//calculate loop size by iterating until public key is reached
			val = (val * 7)%20201227;
		val = 1;	//reset val to 1
		for (int i = 0; i < loop; i++)	//calculate the key by transforming the doors public key with the calculated loop size
			val = (val * in[1])% 20201227;
		return val;
	}

	static String task2() {
		return "Merry Christmas :)";	//nothing left to do here :)
	}
}