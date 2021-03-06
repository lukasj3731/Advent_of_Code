public class AOC02 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static int task1() {
		String[] pwds = StringArrInput("inputs/input02.txt");
		int valid=0;
		for(int i=0;i<pwds.length;i++)	// min <= count <= max
			valid += between(pInt(pwds[i].split("-")[0]),
							countChar(pwds[i].split(":")[1],pwds[i].charAt(pwds[i].indexOf(':')-1)),
							pInt(pwds[i].split("-")[1].split(" ")[0]))?1:0;
		return valid;
	}

	static int task2() {
		String[] pwds = StringArrInput("inputs/input02.txt");
		int valid=0;	
		for(int i=0;i<pwds.length;i++) {	//xor (charAt minPos correct, charAt maxPos correct)
			char c = pwds[i].charAt(pwds[i].indexOf(':')-1);
			valid += xor(pwds[i].split(":")[1].charAt(pInt(pwds[i].split("-")[0]))==c,
					pwds[i].split(":")[1].charAt(pInt(pwds[i].split("-")[1].split(" ")[0]))==c)?1:0;
		}
		return valid;
	}
}