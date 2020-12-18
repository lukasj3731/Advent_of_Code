public class AOC18 extends AOC {
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
		long sum = 0;
		for(String line:StringArrInput("inputs/input18.txt"))	//for every line in input
			sum += pLong(eval(line, t2));		//add evaluated expression to sum
		println("Task "+(t2?2:1)+": "+sum);
	}

	static String eval(String s, boolean t2) {
		while(s.contains("(")) {
			String parenth = regexFinder("\\(([^()]+)\\)", s);		//finds any expression in parenthesis
			s = s.replace("("+parenth+")", eval(parenth, t2));	//evaluates expression and substitutes it with solution
		}
		if(t2) {	//for task 2:
			long prod = 1;
			for(String addition:s.split(" \\* ")) {	//find all additions
				long sum = 0;
				for(String nums:addition.split(" \\+ "))
					sum += pLong(nums);	//add all numbers
				prod *= sum;	//multiply additions together
			}
			return ""+prod;
		} else {	//for task 1:
			String[] operators = s.split(" ");
			long total = pLong(operators[0]);	//takefirst number
			for(int i=1;i<operators.length;i+=2)	//for every other number
				total = operators[i].contains("+")?	//if operator is plus, add otherwise multiply
						total + pLong(operators[i+1]):total * pLong(operators[i+1]);
			return ""+total;
		}
	}
}