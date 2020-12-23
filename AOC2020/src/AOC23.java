import java.util.Arrays;
import java.util.HashMap;
public class AOC23 extends AOC{

	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static void iterate(HashMap<Integer, RingNode> map, RingNode curr ,int iterations) {
		for(int i=0;i<iterations;i++) {	//for number of iterations
			RingNode group = curr.next;	//get group to be displaced
			curr.next = group.next.next.next;	//unlink group from ring
			RingNode goal = null;
			for(int off = 1;goal == null;off++) {	//find goal Node
				int m = curr.val-off;
				if(m<=0)
					m += map.size();	//can't be negative or 0
				goal = map.get(m);
				if(group == goal || group.next == goal || group.next.next == goal)	//can't be within group
					goal = null;
			}
			group.next.next.next=goal.next;	//insert next of goal after group
			goal.next=group;	//insert group after goal
			curr = curr.next;	//go to next
		}
	}
	
	static HashMap<Integer, RingNode> generateMap(boolean t2,int[] in) {
		HashMap<Integer, RingNode> map = new HashMap<Integer, RingNode>();
		if(t2)	//for task 2: add 1000000 numbers all linked to each other
			for(int i=1000000;i>in.length;i--)
				map.put(i, new RingNode(i,map.get(i+1)));
		map.put(in[in.length-1], new RingNode(in[in.length-1],map.get(in.length+1)));	//link highest node to null or already inserted node
		for(int i=in.length-2;i>=0;i--)
			map.put(in[i], new RingNode(in[i],map.get(in[i+1])));	//add input nodes linked to each other
		map.get(!t2?in[in.length-1]:1000000).next = map.get(in[0]);	//close the ring
		return map;
	}

	static String task1() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		HashMap<Integer, RingNode> map = generateMap(false, in);
		iterate(map,map.get(in[0]),100);	//iterate 100 times
		String ret="";
		RingNode one = map.get(1);	//get item 1
		do {
			ret += (one=one.next).val;	//add numbers following node '1' to return String till '1' is reached again
		} while(!one.next.equals(map.get(1)));
		return ret;
	}
	
	static long task2() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		HashMap<Integer, RingNode> map = generateMap(true, in);
		iterate(map,map.get(in[0]),10000000);
		return 1l*map.get(1).next.val*map.get(1).next.next.val;	//multiply numbers following the '1'
	}
}