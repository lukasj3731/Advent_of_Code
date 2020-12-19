import java.util.ArrayList;
import java.util.List;

public class AOC08 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static String task1() {
		return exitCode(StringArrInput("inputs/input08.txt")).split(",")[1];
	}

	static String task2() {
		String[] inb = StringArrInput("inputs/input08.txt");
		for(int i=0;i<inb.length;i++) {
			String[] in = inb.clone();
			in[i] = in[i].contains("jmp")?in[i].replaceAll("jmp", "nop"):in[i].replace("nop", "jmp");
			String ret = exitCode(in);
			if(ret.contains("ter"))
				return ret.split(",")[1];
		}
		return "err";
	}
	
	static String exitCode(String[] in){
		int pos = 0, acc = 0;
		List<Integer> m = new ArrayList<Integer>();
		while(!m.contains(pos)) {
			if(pos == in.length)
				return "ter,"+acc+","+pos;		//terminated
			m.add(pos);
			switch(regexFinder("([a-z]*)", in[pos])) {
			case "acc": acc += pInt(regexFinder("[a-z]* ([+-][0-9]*)", in[pos++])); break;
			case "jmp": pos += pInt(regexFinder("[a-z]* ([+-][0-9]*)", in[pos])); break;
			default: pos++;
			}
		}
		return "rep,"+acc+","+pos;	//repeated
	}
}