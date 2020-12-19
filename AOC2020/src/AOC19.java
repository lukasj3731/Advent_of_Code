import java.util.HashMap;

public class AOC19 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		String in = StrInput("inputs/input19.txt");

		String[] rules = in.split("\n\n")[0].split("\n");
		String[] lines = in.split("\n\n")[1].split("\n");
		HashMap<Integer, String> m = new HashMap<Integer,String>();

		for(String line: rules) {
			m.put(pInt(line.split(": ")[0]),line.split(": ")[1]);
		}
		String r = getRegex(0,m, false);
		int sum = 0;
		for(String l:lines)
			sum += l.matches(r)?1:0;
		println("Task 1: "+sum);
	}

	
	
	static String getRegex(int rule, HashMap<Integer, String> m, boolean t2) {
		
		if(rule == 8 && t2) {
			return "("+getRegex(42, m, t2)+"+)";
		} else if(rule == 11 && t2) {
        	String r42 = getRegex(42,m,t2);
        	String r31 = getRegex(31,m,t2);
        	
        	String ret = "(";
        	for(int i=1;i<10;i++) {
        		ret += "("+r42+"{"+i+"}"+r31+"{"+i+"})|";
        	}
        	ret = ret.substring(0, ret.length()-1)+")";
        	return ret;
        }
		
		String r = m.get(rule);
		if(r.contains("\"")) {
			return r.replaceAll("\"", "");
		}
		
		String ret = "(";
		for(String s:r.split(" ") ){
			if(s.equals("|")) {
				ret += "|";
			} else {
				ret += getRegex(pInt(s),m, t2);
			}
		}
		return ret +")";
	}
	
	
	
	static void task2() {
		String in = StrInput("inputs/input19.txt");

		String[] rules = in.split("\n\n")[0].split("\n");
		String[] lines = in.split("\n\n")[1].split("\n");
		HashMap<Integer, String> m = new HashMap<Integer,String>();

		for(String line: rules) {
			m.put(pInt(line.split(": ")[0]),line.split(": ")[1]);
		}
		String r = getRegex(0,m, true);
		int sum = 0;
		for(int i=0;i<lines.length;i++) {
			String test = lines[i];
			//test = m.get(0).match(test,m, test.length());
			if(test.matches(r)) {
				sum++;
			}
		}
		println("Task 1: "+sum);
	}
}