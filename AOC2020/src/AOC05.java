import java.util.LinkedList;
import java.util.List;

public class AOC05 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		int max = 0;
		for(String s:StringArrInput("inputs/input05.txt"))
			max = Math.max(getBin(s.substring(0, 7),'B')*8+getBin(s.substring(7, 10),'R'),max);	
		println("Task 1: "+max);
	}

	static void task2() {
		List<Integer> l = new LinkedList<Integer>();
		for(String s:StringArrInput("inputs/input05.txt"))
			l.add(getBin(s.substring(0, 7),'B')*8+getBin(s.substring(7, 10),'R'));
		int id=0;
		for(;!(l.contains(id-1)&&l.contains(id+1)&&!l.contains(id))&&id<9999;id++) {}	//the id<9999 is unneccessary, but i feel safer that way
		println("Task 2: "+id);
	}

	static int getBin(String in, char one) {	//turns a string of symbols into binary, where <one> indicates a 1 and any other symbol a 0
		int id=0;
		for(int i=0;i<in.length();i++)
			id=2*id+(in.charAt(i)==one?1:0);
		return id;
	}
}