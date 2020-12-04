public class AOC04 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		int valid = 0;
		for(String p:StrInput("inputs/input04.txt").split("\n\n"))
			valid += (p.split("[\n ]").length+(!p.contains("cid")?1:0)==8)?1:0;
		println("Task 1: "+valid);
	}
	
	static void task2() {
		int valid = 0;
		for(String p:StrInput("inputs/input04.txt").split("\n\n")) {
			boolean c = true;
			for(String n:p.split("[\n ]"))
				c = isValid(p,regexFinder("([a-z]{3}):",n))?c:false;
			valid += (c&&(p.split("[\n ]").length+(!p.contains("cid")?1:0)==8))?1:0;
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
		case "ecl": return regexFinder("ecl:(amb|blu|brn|gry|grn|hzl|oth)",p).length()>0;
		default: return regexFinder("pid:([0-9]*)",p).length()==9; //pid
		}
	}
	
	static boolean regexBetween(String reg, String p, int min, int max) {
		return regexFinder(reg,p).length()==0?false:between(min,pInt(regexFinder(reg,p)),max);
	}
}