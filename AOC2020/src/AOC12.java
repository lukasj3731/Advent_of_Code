public class AOC12 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		char dirTotal = 'E';
		int[] NESW = new int[4];
		for(String s: StringArrInput("inputs/input12.txt")) {
			char dir = s.charAt(0);
			int val = pInt(s.substring(1));
			if("RL".contains(""+dir)) 
				dirTotal = "NESW".charAt(("NESW".indexOf(dirTotal)+(dir=='R'?val:-val)/90+4)%4);	//if operation is L or R, rotate accordingly
			else 
				NESW["NESW".indexOf(dir=='F'?dirTotal:dir)] += val;	//otherwise, move ship accordingly
		}
		println("Task 1: "+(Math.abs(NESW[0]-NESW[2])+Math.abs(NESW[1]-NESW[3])));
	}
	
	static void task2() {
		Point shipPos = new Point(0,0),waypoint = new Point(1,10);
		for(String s: StringArrInput("inputs/input12.txt")) {
			char dir = s.charAt(0);
			int val = pInt(s.substring(1));
			switch(dir) {
			case 'N': waypoint.x += val; break;
			case 'E': waypoint.y += val; break;
			case 'S': waypoint.x -= val; break;
			case 'W': waypoint.y -= val; break;
			case 'F': shipPos = shipPos.add(waypoint.scale(val)); break;
			default: 
				for(int i=0;i<val/90;i++)
					waypoint.x = (dir=='L'?1:-1)*(waypoint.y-waypoint.x)-(waypoint.y=waypoint.x*(dir=='L'?-1:1)); //waypoint-rotate-one-liner (don't even ask)
			}
		}
		println("Task 2: "+(Math.abs(shipPos.x)+Math.abs(shipPos.y)));
	}
}