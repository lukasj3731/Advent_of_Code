import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AOC18 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String[] in = StringArrInput("inputs/input18.txt");
		long sum = 0;
		for(int i=0;i<in.length;i++) {
			String parenth = evalParenth(in[i]);
			sum += pLong(parenth);
		}
		println("Task 1: "+sum);
	}
	
	static String evalParenth(String s) {
		//println("parenth "+s);
		while(s.contains("(")) {
			//println("entered loop");
			String parenth = regexFinder("\\(([^()]+)\\)", s);
			//println(parenth);
			s=s.replace("("+parenth+")", evalParenth(parenth));
			//println(s);
		}
		return eval(s);
	}
	
	static String eval(String s) {
		//println("eval "+s);
		String[] operators = s.split(" ");
		long total = pLong(operators[0]);
		
		for(int i=1;i<operators.length;i+=2) {
			if(operators[i].contains("+")) {
				total += pLong(operators[i+1]);
			} else {
				total *= pLong(operators[i+1]);
			}
		}
		//println(total);
		return ""+total;
	}
	
	static String evalParenth2(String s) {
		//println("parenth "+s);
		while(s.contains("(")) {
			//println("entered loop");
			String parenth = regexFinder("\\(([^()]+)\\)", s);
			//println(parenth);
			s=s.replace("("+parenth+")", evalParenth2(parenth));
			//println(s);
		}
		return eval2(s);
	}
	
	static String eval2(String s) {
		String[] additions = s.split("\\*");
		long mult = 1;
		for(String l:additions) {
			if(l.charAt(0)==' ') {
				l=l.substring(1);
			}
			if(l.charAt(l.length()-1)==' ') {
				l=l.substring(0,l.length()-1);
			}
			//println(l);
			String[] operators = l.split(" ");
			long total = pLong(operators[0]);
			for(int i=1;i<operators.length;i+=2) {
				if(operators[i].contains("+")) {
					total += pLong(operators[i+1]);
				} else {
					total *= pLong(operators[i+1]);
				}
			}
			mult *= total;
		}
		
		return ""+mult;
	}

	static void task2() {
		String[] in = StringArrInput("inputs/input18.txt");
		long sum = 0;
		for(int i=0;i<in.length;i++) {
			String parenth = in[i];
			parenth = evalParenth2(parenth);
			//println(parenth);
			sum += pLong(parenth);
			//println(parenth);
		}
		println("Task 2: "+sum);
	}
	
	static String regexParenth(String regex, String search) {
		Pattern pattern = Pattern.compile(regex);
		Matcher matcher = pattern.matcher(search);
		for(int i=0;i<matcher.groupCount();i++) {
			search = search.replace(matcher.group(i), "("+matcher.group(i)+")");
		}
		return search;
	}
}