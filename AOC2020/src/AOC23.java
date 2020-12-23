import java.util.Arrays;
import java.util.HashMap;
public class AOC23 extends AOC{

	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static String task1() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		HashMap<Integer, Node> map = new HashMap<Integer, Node>();
		map.put(in[in.length-1], new Node(in[in.length-1],null));
		for(int i=in.length-2;i>=0;i--)
			map.put(in[i], new Node(in[i],map.get(in[i+1])));
		map.get(in[in.length-1]).next = map.get(in[0]);
		Node curr=map.get(in[0]);
		
		for(int i=0;i<100;i++) {
			Node group = curr.next;
			curr.next = group.next.next.next;
			Node goal = null;
			for(int off = 1;goal == null;off++) {
				int m = curr.val-off;
				if(m<=0) {
					m += in.length;
				}
				goal = map.get(m);
				if(group == goal || group.next == goal || group.next.next == goal) {
					goal = null;
				}
			}
			Node newNext = goal.next;
			goal.next=group;
			group.next.next.next=newNext;
			curr = curr.next;
		}
		String ret="";
		Node one = map.get(1).next;
		while(!one.equals(map.get(1))){
			ret += one.val;
			one = one.next;
		}
		return ret;
	}
	
	static long task2() {
		int[] in = Arrays.stream(StrInput("inputs/input23.txt").split("")).mapToInt(Integer::parseInt).toArray();
		HashMap<Integer, Node> map = new HashMap<Integer, Node>();
		map.put(1000000, new Node(1000000,null));
		for(int i=1000000-1;i>in.length;i--) {
			map.put(i, new Node(i,map.get(i+1)));
		}
		map.put(in[in.length-1], new Node(in[in.length-1],map.get(in.length+1)));
		for(int i=in.length-2;i>=0;i--) {
			map.put(in[i], new Node(in[i],map.get(in[i+1])));
		}
		map.get(1000000).next = map.get(in[0]);
		
		Node curr=map.get(in[0]);
		
		for(int i=0;i<10000000;i++) {
			
			
			//println(map);
			
			Node group = curr.next;
			curr.next = group.next.next.next;
			
			Node goal = null;
			for(int off = 1;goal == null;off++) {
				int m = curr.val-off;
				if(m<=0) {
					m += 1000000;
				}
				goal = map.get(m);
				if(group == goal || group.next == goal || group.next.next == goal) {
					goal = null;
				}
			}
		
			Node newNext = goal.next;
			goal.next=group;
			group.next.next.next=newNext;
			curr = curr.next;
			
			
		}
		Node one = map.get(1);
		return 1l*one.next.val*one.next.next.val;
	}

	static class Node {
		int val=0;
		Node next;
		
		public Node(int val, Node next) {
			this.val = val;
			this.next = next;
		}
		
		public String toString() {
			return ""+val;
		}
	}
}


