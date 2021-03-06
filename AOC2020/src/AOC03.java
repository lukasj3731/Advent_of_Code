public class AOC03 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static int task1() {
		return hitTrees(new Point(1,3), charArrInput("inputs/input03.txt"));
	}

	static long task2() {
		char[][] map = charArrInput("inputs/input03.txt");
		Point[] slopes = {new Point(1,1),new Point(1,3),new Point(1,5),new Point(1,7),new Point(2,1)};
		long prod = 1;
		for(Point s:slopes)
			prod *= hitTrees(s,map);
		return prod;
	}
	
	static int hitTrees(Point slope, char[][] map) {	//number of trees hit at certain slope
		Point pos = new Point(0,0,0,0,"");	//x,y,z,val,name (z and name are irrelevant for this)
		while(pos.x < map.length) {
			pos.val += map[pos.x][pos.y%map[0].length]=='#'?1:0;
			pos = pos.add(slope);
		}
		return pos.val;
	}	
}