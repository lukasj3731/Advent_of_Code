import java.util.Arrays;
public class AOC23 extends AOC{

	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int[] iterate(int[] map, int curr ,int iterations) {
		for(int i=0;i<iterations;i++) {	//for number of iterations
			int group = map[curr];	//get group to be displaced
			map[curr] = map[map[map[group]]];	//unlink group from ring
			int goal = 0;
			for(int off = 1;goal == 0;off++) {	//find goal Node
				int m = curr-off;
				if(m<=0)
					m += map.length-1;	//can't be negative or 0
				goal = m;
				if(group == goal || map[group] == goal || map[map[group]] == goal)	//can't be within group
					goal = 0;
			}
			map[map[map[group]]]=map[goal];	//insert next of goal after group
			map[goal] = group;	//insert group after goal
			curr = map[curr];	//go to next
		}
		return map;
	}
	
	static int[] generateMap(boolean t2,int[] in) {
		int[] map = new int[t2?1000001:in.length+1];
		if(t2) {	//for task 2: add 1000000 numbers all linked to each other
			for(int i=1000000;i>in.length;i--)
				map[i] = i+1;
			map[in[in.length-1]] = in.length+1;	//link highest node to 0 or already inserted node
		}
		for(int i=in.length-2;i>=0;i--)
			map[in[i]] = in[i+1];	//add input nodes linked to each other
		map[!t2?in[in.length-1]:1000000] = in[0];	//close the ring
		return map;
	}

	static String task1() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		int[] map = iterate(generateMap(false, in),in[0],100);	//iterate 100 times
		String ret="";
		int curr = 1;	//get item 1
		do {
			ret += (curr=map[curr]);	//add numbers following node '1' to return String till '1' is reached again
		} while(map[curr]!=1);
		return ret;
	}
	
	static long task2() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		int[] map = iterate(generateMap(true, in),in[0],10000000);
		return 1l*map[1]*map[map[1]];	//multiply numbers following the '1'
	}
}