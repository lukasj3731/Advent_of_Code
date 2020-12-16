public class AOC16 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String in = StrInput("inputs/input16.txt");
		
		String[] conditions = in.split("\n\n")[0].split("\n");
		Condition[] c = new Condition[conditions.length];
		for(int i=0;i<conditions.length;i++) {
			c[i]=(new Condition(conditions[i]));
		}
		
		int sum = 0;
		
		String[] tickets = in.split("\n\n")[2].split("\n");
		for(int i=1;i<tickets.length;i++) {
			String[] nums = tickets[i].split(",");
			for(String s:nums) {
				
				boolean matchesAny = false;
				for(int j=0;j<c.length;j++) {
					if(c[j].maches(pInt(s))) {
						matchesAny=true;
						//println("found "+s+" in "+c[j]);
					}
				}
				if(!matchesAny){
					sum += pInt(s);
					//println(s);
				}
				
			}
		}
		println("Task 1: "+sum);
	}
	
	static void task2() {
		String in = StrInput("inputs/input16.txt");
		
		String[] conditions = in.split("\n\n")[0].split("\n");
		Condition[] c = new Condition[conditions.length];
		for(int i=0;i<conditions.length;i++) {
			c[i]=(new Condition(conditions[i]));
		}
		
		String corrected = "";
		
		String[] tickets = in.split("\n\n")[2].split("\n");
		for(int i=1;i<tickets.length;i++) {
			
			boolean allValid=true;
			
			String[] nums = tickets[i].split(",");
			for(String s:nums) {
				boolean matchesAny = false;
				for(int j=0;j<c.length;j++) {
					if(c[j].maches(pInt(s))) {
						matchesAny=true;
					}
				}
				if(!matchesAny){
					allValid = false;
				}
				
			}
			
			if(allValid) {
				corrected+= tickets[i]+"\n";
			}
		}
		corrected = corrected.substring(0, corrected.length()-1);
		String[] lines = corrected.split("\n");
		String[] possible = new String[countChar(lines[0], ',')+1];
		for(int i=0;i<countChar(lines[0], ',')+1;i++) {
			possible[i] = "";
			for(Condition cond:c) {
				boolean matchesAll = true;
				for(int j=0;j<lines.length;j++) {
					if(!cond.maches(pInt(lines[j].split(",")[i]))) {
						matchesAll = false;
					}
				}
				if(matchesAll) {
					possible[i] += cond.name+",";
				}
			}
			possible[i] = possible[i].substring(0,possible[i].length()-1);
		}
		
		while(!unique(possible)) {
		//for(int a=0;a<10;a++) {
			int lastUnique=-1;
			for(int i=0;i<possible.length;i++) {
				if(!possible[i].contains(","))
					lastUnique = i;
				
				for(int j=0;j<possible.length;j++) {
					if(j!=i) {
						possible[j]=possible[j].replaceAll(possible[i], "");
						possible[j].replaceAll(",,", ",");
						if(possible[j].charAt(0)==',') {
							possible[j] = possible[j].substring(1);
						} else if(possible[j].charAt(possible[j].length()-1)==',') {
							possible[j] = possible[j].substring(0,possible[j].length()-1);
						}
					}
				}
			}
		}
		//println(possible);
		long prod = 1;
		for(int i=0;i<possible.length;i++) {
			if(possible[i].contains("departure")) {
				prod *= pInt(in.split("\n\n")[1].split("\n")[1].split(",")[i]);
				//println(i+": "+pInt(in.split("\n\n")[1].split("\n")[1].split(",")[i]));
			}
		}
		//println(corrected);
		println("Task 2: "+prod);
	}
	
	static class Condition {
		Point r1, r2;
		String name;
		public Condition (String line) {
			this.r1 = new Point(pInt(regexFinder(".*: ([0-9]*)",line)),pInt(regexFinder(".*: [0-9]*-([0-9]*)",line)));
			this.r2 = new Point(pInt(regexFinder(".*:.*or ([0-9]*)",line)),pInt(regexFinder(".*:.*or.*-([0-9]*)",line)));
			this.name = regexFinder("(.*):",line);
		}
		
		public String toString() {
			return r1.toString()+" | "+r2.toString();
		}
		
		public boolean maches(int n) {
			return between(r1.x,n,r1.y) || between(r2.x,n,r2.y);
		}
	}
	
	static boolean unique(String[] in) {
		for(String s:in) {
			if (s.contains(","))
				return false;
		}
		return true;
	}
}