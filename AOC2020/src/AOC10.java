import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AOC10 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static int task1() {
		List<Integer> l = intListInput("inputs/input10.txt");
		l.add(0);
		l.sort(null);
		int[] diffs = {0,1};	//the one is because of the 3 jolts diff when connecting to the laptop
		for(int i=0;i<l.size()-1;i++)
			for(int d=0;d<=1;d++)
				diffs[d] += (l.get(i+1)-l.get(i)==1+2*d)?1:0;	//if diff 1 or 3 is valid, add to diffs
		return diffs[0]*diffs[1];
	}

	static long task2() {		//got a complaint my code isn't very understandable. daniel, this excessive commenting is your fault
		List<Integer> l = intListInput("inputs/input10.txt");	//reading the input file into a list called l
		l.add(0);	//adding 0 to this list. this element is equivalent to the wall outlet
		l.sort(null);	//sorting the list so that the smallest element is first and the biggest element is last
		l.add(l.get(l.size()-1)+3);	//adding the laptop to the list. the laptop is 3 jolts over the biggest (aka the last) element in the list
		Map<Integer, Long> m = new HashMap<Integer, Long>();	//initializing a list. it maps from a chargers jolts to the possibilities of plugs after it. e.g.: [10->5962] means there is 5962 ways to plug the laptop into a charger with 10 jolts
		for(int i=l.size()-1;i>=0;i--) {	//moving backwards through list, starting with the laptop
			long total = i==l.size()-1?1:0;	//the laptop is initialized with one possibility, all other elements start with 0. thats cause the laptop has nothing it has to be plugged into
			for(int j=1;j<=3;j++)	//iterating through every reachable adapter from the current one (those are adapters with jolts+1, jolts+2 and jolts+3)
				total += (m.containsKey(l.get(i)+j))?m.get(l.get(i)+j):0;	//if such an adapter exists, the possible ways to plug it in are added to the total.
			m.put(l.get(i), total);	//the total is then added to the map, so that future adapters can use it's value for calculation
		}	//here I'm closing a bracket
		return m.get(0);	//lastly, we print the possibilities to plug into the outlet. this number equals all possible charger arrangements between outlet and laptop
	}
}