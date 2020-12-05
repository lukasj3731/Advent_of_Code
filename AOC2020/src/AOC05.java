import java.util.LinkedList;
import java.util.List;

public class AOC05 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		int max = -1;
		for(String s:StringArrInput("inputs/input05.txt"))
			max = Math.max(getBin(s.substring(0, 7),'B')*8+getBin(s.substring(7, 10),'R'), max);	
		println("Task 1: "+max);
	}

	static void task2() {
		List<Integer> l = new LinkedList<Integer>();
		for(String s:StringArrInput("inputs/input05.txt"))
			l.add(getBin(s.substring(0, 7),'B')*8+getBin(s.substring(7, 10),'R'));
		int i=0;
		for(;!(l.contains(i-1)&&l.contains(i+1)&&!l.contains(i));i++) {}
		println("Task 2: "+i);
	}

	static int getBin(String in, char one) {
		int id=0;
		for(int i=0;i<in.length();i++)
			id=2*id+(in.charAt(i)==one?1:0);
		return id;
	}
}