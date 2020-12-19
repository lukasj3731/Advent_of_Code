import java.util.LinkedList;
import java.util.List;

public class AOC05 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static int task1() {
		int max = 0;
		for(String s:StringArrInput("inputs/input05.txt"))
			max = Math.max(binaryFromString(s.substring(0, 7),'B')*8+binaryFromString(s.substring(7, 10),'R'),max);	
		return max;
	}

	static int task2() {
		List<Integer> l = new LinkedList<Integer>();
		for(String s:StringArrInput("inputs/input05.txt"))
			l.add(binaryFromString(s.substring(0, 7),'B')*8+binaryFromString(s.substring(7, 10),'R'));
		int id=0;
		for(;!(l.contains(id-1)&&l.contains(id+1)&&!l.contains(id))&&id<9999;id++) {}	//the id<9999 is unneccessary, but I feel safer that way
		return id;
	}
}