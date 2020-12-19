import java.util.HashMap;

public class AOC19 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int task1() {
		return task(false);
	}
	
	static int task2() {
		return task(true);
	}
	
	static int task(boolean t2) {
		String in = StrInput("inputs/input19.txt");
		HashMap<Integer, String> m = new HashMap<Integer,String>();	//maps [ruleNumber -> ruleSet]
		for(String rule: in.split("\n\n")[0].split("\n"))
			m.put(pInt(rule.split(":")[0]),rule.split(": ")[1]);	//add every rule to map
		String r = getRegex(0,m,t2);	//generate regex for ruleset
		int sum = 0;
		for(String line:in.split("\n\n")[1].split("\n"))	//increment sum if line matches regex
			sum += line.matches(r)?1:0;
		return sum;
	}

	static String getRegex(int rule, HashMap<Integer, String> m, boolean t2) {
		if(rule == 8 && t2)	//for task 2: rule 8 is (rule42)+
			return "("+getRegex(42, m, t2)+"+)";
		if(rule == 11 && t2) {	//for task 2: rule 11 is (rule42{n} rule31{n}) where n is an integer between 1 and 20 (20 is just an assumption, I hope this always works?)
        	String c1 = getRegex(42,m,t2);
        	String c2 = getRegex(31,m,t2);
        	String ret = "(";
        	for(int i=1;i<20;i++)
        		ret += "("+c1+"{"+i+"}"+c2+"{"+i+"})|";
        	return ret.substring(0, ret.length()-1)+")";
        }
		String r = m.get(rule);		//for every other rule
		if(r.contains("\""))	//if it contains ", it's a terminator, so 'a' or 'b'
			return r.replaceAll("\"", "");
		String ret = "(";
		for(String s:r.split(" ") )	//otherwise add 'or' separated regexes
			ret += s.equals("|")?"|":getRegex(pInt(s),m, t2);
		return ret +")";
	}	//i could use a map for memorizing regexes but the regex generation is not taking long compared to the evaluation so I didn't bother
}