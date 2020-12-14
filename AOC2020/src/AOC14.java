import java.util.HashMap;
import java.util.Map;

public class AOC14 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String[] in = StringArrInput("inputs/input14.txt");
		String mask = "";
		Map<Integer,Long> m = new HashMap<Integer, Long>();
		for(String s:in) {
			if(s.contains("mask")) {
				mask = s.substring(7);
			} else {
				int addr = pInt(regexFinder("mem\\[([0-9]*)\\].*", s));
				int val = pInt(regexFinder(".* ([0-9]*)",s));
				m.put(addr, mask(val,mask));
			}
		}
		long sum = 0;
		for(int k:m.keySet()) {
			sum += m.get(k);
		}
		println("Task 1: "+sum);
	}

	static void task2() {
		String[] in = StringArrInput("inputs/input14.txt");
		String mask = "";
		Map<Long,Long> m = new HashMap<Long, Long>();
		for(String s:in) {
			if(s.contains("mask")) {
				mask = s.substring(7);
			} else {
				int addr = pInt(regexFinder("mem\\[([0-9]*)\\].*", s));
				int val = pInt(regexFinder(".* ([0-9]*)",s));
				recWrite(mask2(addr,mask),val,m);
			}
		}
		long sum = 0;
		for(Long k:m.keySet()) {
			sum += m.get(k);
		}
		println("Task 1: "+sum);
	}
	
	static long mask(int num, String mask) {
		String binary = Integer.toBinaryString(num);
		binary = String.format("%36s",binary);
		binary = binary.replace(' ','0');
		String ret = "";
		for(int i=0;i<binary.length();i++) {
			if(mask.charAt(i)=='X') {
				ret += binary.charAt(i);
			} else {
				ret += mask.charAt(i);
			}
		}
		return binaryFromStringLong(ret, '1');
	}
	
	static String mask2(int num, String mask) {
		String binary = Integer.toBinaryString(num);
		binary = String.format("%36s",binary);
		binary = binary.replace(' ','0');
		String ret = "";
		for(int i=0;i<binary.length();i++) {
			if(mask.charAt(i)=='0') {
				ret += binary.charAt(i);
			} else {
				ret +=  mask.charAt(i);
			}
		}
		return ret;
	}
	
	static void recWrite(String addr, long val, Map<Long, Long> m) {
		if(!addr.contains("X")) {
			m.put(binaryFromStringLong(addr, '1'), val);
		} else {
			recWrite(addr.replaceFirst("X", "1"),val,m);
			recWrite(addr.replaceFirst("X", "0"),val,m);
		}
	}
	
	static long binaryFromStringLong(String in, char one) {	//turns a string of symbols into binary, where <one> indicates a 1 and any other symbol a 0
		long number=0;
		for(int i=0;i<in.length();i++)
			number=2*number+(in.charAt(i)==one?1:0);
		return number;
	}
}