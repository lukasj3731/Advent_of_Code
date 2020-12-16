public class AOC16 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String in = StrInput("inputs/input16.txt");
		String[] conditions = in.split("\n\n")[0].split("\n");
		Condition[] c = new Condition[conditions.length];
		for(int i=0;i<conditions.length;i++)	//turn list of ticket-field rules into condition
			c[i]=(new Condition(conditions[i]));
		int sum = 0;
		String[] tickets = in.split("\n\n")[2].split("\n");
		for(int i=1;i<tickets.length;i++) {	//for every ticket
			String[] nums = tickets[i].split(",");
			for(String s:nums) {
				boolean matchesAny = false;
				for(int j=0;j<c.length;j++)		//see if any numer does not match any condition
					matchesAny = c[j].maches(pInt(s))?true:matchesAny;
				sum += matchesAny?0:pInt(s);	//and add that numbber to the sum
			}
		}
		println("Task 1: "+sum);
	}
	
	static void task2() {
		String in = StrInput("inputs/input16.txt");
		String[] conditions = in.split("\n\n")[0].split("\n");
		Condition[] c = new Condition[conditions.length];
		for(int i=0;i<conditions.length;i++)	//turn list of ticket-field rules into condition
			c[i]=(new Condition(conditions[i]));
		String corrected = "";
		String[] tickets = in.split("\n\n")[2].split("\n");
		for(int i=1;i<tickets.length;i++) {	//for all tickets
			boolean allValid=true;
			String[] nums = tickets[i].split(",");
			for(String s:nums) {
				boolean matchesAny = false;
				for(int j=0;j<c.length;j++)	//see if any numbers are false;
					matchesAny = c[j].maches(pInt(s))?true:matchesAny;
				allValid = matchesAny?allValid:false;
			}
			corrected += allValid?tickets[i]+"\n":"";	//if all are valid, add to corrected string
		}
		String[] lines = corrected.substring(0, corrected.length()-1).split("\n");
		String[] possible = new String[countChar(lines[0], ',')+1];	//array if strings containing possible fields separated by "," for every index
		for(int i=0;i<countChar(lines[0], ',')+1;i++) {	//for every column
			possible[i] = "";
			for(Condition cond:c) {	//test every condition
				boolean matchesAll = true;
				for(int j=0;j<lines.length;j++)
					matchesAll = cond.maches(pInt(lines[j].split(",")[i]))?matchesAll:false;
				possible[i] += matchesAll?cond.name+",":"";	//if the condition matches every line, add field to possible
			}
			possible[i] = possible[i].substring(0,possible[i].length()-1);
		}
		while(!unique(possible))	//while not every field is unique
			for(int i=0;i<possible.length;i++)	//take one field
				for(int j=0;j<possible.length;j++)	//and remove it's occurence from every other possible list
					if(j!=i) {
						possible[j] = possible[j].replaceAll(possible[i], "").replaceAll(",,", ",");
						possible[j] = possible[j].substring(possible[j].charAt(0)==','?1:0,
								possible[j].charAt(possible[j].length()-1)==','?possible[j].length()-1:possible[j].length());
					}
		long prod = 1;
		for(int i=0;i<possible.length;i++)	//multiply product together
				prod *= possible[i].contains("departure")?pInt(in.split("\n\n")[1].split("\n")[1].split(",")[i]):1;
		println("Task 2: "+prod);
	}
	
	static class Condition {	//takes a line and turns it into condition with the bounds and the fields name
		Point r1, r2;
		String name;
		public Condition (String line) {
			this.r1 = new Point(pInt(regexFinder(".*: ([0-9]*)",line)),pInt(regexFinder(".*: [0-9]*-([0-9]*)",line)));
			this.r2 = new Point(pInt(regexFinder(".*:.*or ([0-9]*)",line)),pInt(regexFinder(".*:.*or.*-([0-9]*)",line)));
			this.name = regexFinder("(.*):",line);
		}
		
		public boolean maches(int n) {
			return between(r1.x,n,r1.y) || between(r2.x,n,r2.y);
		}
	}
	
	static boolean unique(String[] in) {	//tests if every line only contains one item
		for(String s:in)
			if (s.contains(","))
				return false;
		return true;
	}
}