import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class AOC22 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static long task1() {
		String in = StrInput("inputs/input22.txt");
		String[] players = in.split("\n\n");
		Queue<Integer> p1 = new LinkedList<Integer>();
		Queue<Integer> p2 = new LinkedList<Integer>();
		String[] player1 = players[0].split("\n");
		String[] player2 = players[1].split("\n");
		
		for(int i=1;i<player1.length;i++) {
			
			p1.add(pInt(player1[i]));
			p2.add(pInt(player2[i]));
		}
		
		while(p1.size()>0 && p2.size()>0) {
			int card1 = p1.poll();
			int card2 = p2.poll();
			
			if(card1>card2) {
				p1.add(card1);
				p1.add(card2);
			} else {
				p2.add(card2);
				p2.add(card1);
			}
		}
		long sum = 0;
		for(int i=p2.size();i>0;i--) {
			sum += i*p2.poll();
		}
		return sum;
	}
	
	static long task2() {
		String in = StrInput("inputs/input22.txt");
		String[] players = in.split("\n\n");
		Queue<Integer> p1 = new LinkedList<Integer>();
		Queue<Integer> p2 = new LinkedList<Integer>();
		String[] player1 = players[0].split("\n");
		String[] player2 = players[1].split("\n");
		
		for(int i=1;i<player1.length;i++) {
			p1.add(pInt(player1[i]));
		}
		for(int i=1;i<player2.length;i++) {
			p2.add(pInt(player2[i]));
		}
		return Math.abs(subGame(p1,p2));
	}
	
	static long subGame(Queue<Integer> p1, Queue<Integer> p2) {
		HashSet<String> rep = new HashSet<String>();
		while(p1.size()>0 && p2.size()>0) {
			String state = p1.toString()+"|"+p2.toString();
			if(rep.contains(state)) {
				return 1;
			}
			rep.add(state);
			int c1 = p1.poll();
			int c2 = p2.poll();
			
			if(c1>p1.size() || c2>p2.size()) {
				if(c1>c2) {
					p1.add(c1);
					p1.add(c2);
				} else {
					p2.add(c2);
					p2.add(c1);
				}
			} else {
				Queue<Integer> n1 = new LinkedList<Integer>();
				Queue<Integer> n2 = new LinkedList<Integer>();
				Queue<Integer> s1 = new LinkedList<Integer>();
				Queue<Integer> s2 = new LinkedList<Integer>();
				
				while(p1.size()>0) {
					int t = p1.poll();
					if(s1.size()<c1) {
						s1.add(t);
					}
					n1.add(t);
				}
				while(p2.size()>0) {
					int t = p2.poll();
					if(s2.size()<c2) {
						s2.add(t);
					}
					n2.add(t);
				}
				p1 = n1;
				p2 = n2;
				if(subGame(s1, s2)>0) {
					p1.add(c1);
					p1.add(c2);
				} else {
					p2.add(c2);
					p2.add(c1);
				}
			}
		}
		long sum = 0;
		for(int i=p1.size();i>0;i--) {
			sum += i*p1.poll();
		}
		for(int i=p2.size();i>0;i--) {
			sum -= i*p2.poll();
		}
		return sum;
	}
}



