import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class AOC22 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static long task1() {
		return task(false);
	}
	
	static long task2() {
		return task(true);
	}
	
	static long task(boolean t2) {
		String[] players = StrInput("inputs/input22.txt").split("\n\n");
		Queue<Integer> p1 = new LinkedList<Integer>(),p2 = new LinkedList<Integer>();	//make card-queues for each player
		String[] player1 = players[0].split("\n"),player2 = players[1].split("\n");
		for(int i=1;i<player1.length;i++) {	//fill queues
			p1.add(pInt(player1[i]));
			p2.add(pInt(player2[i]));
		}
		return Math.abs(game(p1,p2,t2));	//play game
	}
	
	static long game(Queue<Integer> p1, Queue<Integer> p2, boolean t2) {	//returns score of winner, positive is player1 wins, negative is player2 wins
		HashSet<String> rep = new HashSet<String>();	//set of repetitions
		while(p1.size()*p2.size()>0) {
			String state = p1.toString()+"|"+p2.toString();
			if(rep.contains(state))	//return 1 if repetition occurs
				return 1;
			rep.add(state);	//else save the repetition
			int c1 = p1.poll(),c2 = p2.poll();	//draw top card
			if((c1>p1.size()||c2>p2.size()||!t2)?c1>c2:game(takeN(p1,c1),takeN(p2,c2),t2)>0) {	//depending on who won, give cards to winner
				p1.add(c1);
				p1.add(c2);
			} else {
				p2.add(c2);
				p2.add(c1);
			}
		}
		long sum = 0;	//sum up score of winner
		for(int i=p1.size();i>0;i--)
			sum += i*p1.poll();
		for(int i=p2.size();i>0;i--)
			sum -= i*p2.poll();
		return sum;
	}
}