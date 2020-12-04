public class AOC04 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String[] passports = StrInput("inputs/input04.txt").split("\n\n");
		String[] neccessary = {"byr","iyr","eyr","hgt","hcl","ecl","pid"};
		int valid = 0;
		for(String p:passports) {
			int c = 0;
			for(String n:neccessary)
				c += p.contains(n)?1:0;
			valid += c==neccessary.length?1:0;
		}
		println("Task 1: "+valid);
	}
	
	static void task2() {
		String[] passports = StrInput("inputs/input04.txt").split("\n\n");
		String[] neccessary = {"byr","iyr","eyr","hgt","hcl","ecl","pid"};
		int valid = 0;
		for(String p:passports) {
			int c = 0;
			for(String n:neccessary)
				c += isValid(p,n)?1:0;
			valid += c==neccessary.length?1:0;
		}
		println("Task 2: "+valid);
	}

	private static boolean isValid(String p, String n) {
		switch(n) {
		case "byr": return regexBetween("byr:([0-9]*)",p,1920,2002);
		case "iyr": return regexBetween("iyr:([0-9]*)",p,2010,2020);
		case "eyr": return regexBetween("eyr:([0-9]*)",p,2020,2030);
		case "hgt": return regexBetween("hgt:([0-9]*)in",p,59,76) || regexBetween("hgt:([0-9]*)cm",p,150,193);
		case "hcl": return regexFinder("hcl:(#[a-f0-9]*)",p).length()==7;
		case "ecl": 
			boolean ret = false;
			String[] col = {"amb","blu","brn","gry","grn","hzl","oth"};
			for(String c:col)
				ret = c.equals(regexFinder("ecl:([a-z]*)",p))?true:ret;
			return ret;
		default: return regexFinder("pid:([0-9]*)",p).length()==9; //pid
		}
	}
	
	static boolean regexBetween(String reg, String p, int min, int max) {
		return regexFinder(reg,p).length()==0?false:between(min,pInt(regexFinder(reg,p)),max);
	}
}