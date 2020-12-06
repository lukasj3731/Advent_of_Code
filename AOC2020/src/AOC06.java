public class AOC06 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		int sum = 0;
		for(String answers:StrInput("inputs/input06.txt").split("\n\n"))
			for(char c='a';c<='z';c++)
				sum += answers.contains(c+"")?1:0;
		println("Task 1: "+sum);
	}
	
	static void task2() {
		int sum = 0;
		for(String answers:StrInput("inputs/input06.txt").split("\n\n"))
			for(char c='a';c<='z';c++) {
				int ppl = 0;
				for(String s:answers.split("\n")) 
					ppl += s.contains(c+"")?1:0;
				sum += (ppl==answers.split("\n").length)?1:0;
			}
		println("Task 1: "+sum);
	}
}