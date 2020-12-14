import java.util.HashMap;
import java.util.Map;

public class AOC14 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		task(false);
	}

	static void task2() {
		task(true);
	}

	static void task(boolean t2) {
		String mask = "";
		Map<Long, Long> m = new HashMap<Long, Long>();	//map for [memory address -> value]
		for (String s : StringArrInput("inputs/input14.txt"))
			if (s.contains("mask")) {
				mask = s.substring("mask = ".length());	//update mask
			} else {
				long addr = pInt(regexFinder("mem\\[([0-9]*)\\].*", s));	//read address
				long val = pInt(regexFinder(".* ([0-9]*)", s));		//read value
				if (t2)
					recWrite(mask(addr, mask, t2), val, m);		//task 2: recursive-write value to masked addresses
				else
					m.put(addr, binaryFromStringLong(mask(val, mask, t2), '1'));	//task 1: write masked value to address
			}
		long sum = 0;
		for (long k : m.values())	//sum all values in map
			sum += k;
		println("Task " + (t2 ? 2 : 1) + ": " + sum);
	}

	static String mask(long num, String mask, boolean t2) {
		String ret = "", binary = String.format("%36s", Long.toBinaryString(num)).replace(' ', '0'); //turns number into binary with leading zeros
		for (int i = 0; i < binary.length(); i++)
			ret += (mask.charAt(i) == (t2 ? '0' : 'X') ? binary : mask).charAt(i); //when doing task1/task2 we're reading from binary when seeing a X/0
		return ret;
	}

	static void recWrite(String addr, long val, Map<Long, Long> m) {	//recursively writes to not taken memory addresses
		if (!addr.contains("X")) {
			m.put(binaryFromStringLong(addr, '1'), val);	//if address is unambiguous, write to map
		} else {
			recWrite(addr.replaceFirst("X", "1"), val, m);	//else replace first amiguous 'X' and then try again
			recWrite(addr.replaceFirst("X", "0"), val, m);
		}
	}
}