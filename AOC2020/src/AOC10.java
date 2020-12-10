import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AOC10 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		List<Integer> l = intListInput("inputs/input10.txt");
		l.add(0);
		l.sort(null);
		int[] diffs = {0,1};	//the one is because of the 3 jolts diff when connecting to the laptop
		for(int i=0;i<l.size()-1;i++)
			for(int d=0;d<=1;d++)
				diffs[d] += (l.get(i+1)-l.get(i)==1+2*d)?1:0;	//if diff 1 or 3 is valid, add to diffs
		println("Task 1: "+(diffs[0]*diffs[1]));
	}

	static void task2() {
		List<Integer> l = intListInput("inputs/input10.txt");
		l.add(0);
		l.sort(null);
		l.add(l.get(l.size()-1)+3);
		Map<Integer, Long> m = new HashMap<Integer, Long>();
		for(int i=l.size()-1;i>=0;i--) {	//moving backwards through list
			long total = i==l.size()-1?1:0;	//biggest element starts with 1, others with 0
			for(int j=1;j<=3;j++)	//for every possible adapter
				total += (m.containsKey(l.get(i)+j))?m.get(l.get(i)+j):0;	//add possibilities to total
			m.put(l.get(i), total);	//add total to map
		}
		println("Task 2: "+m.get(0));
	}
}