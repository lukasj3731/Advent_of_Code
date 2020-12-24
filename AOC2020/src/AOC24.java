import java.util.HashMap;

public class AOC24 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int task1() {
		int sum =0;
		for(boolean b:buildFloor().values())	//sum up any black (true) tiles in floor
			sum += b?1:0;
		return sum;
	}

	static int task2() {
		HashMap<Point, Boolean> floor = buildFloor();
		for(int i=0;i<100;i++)	//iterate floor 100 times
			floor = iterate(floor);
		int sum =0;
		for(boolean b:floor.values())	//sum up any black (true) tiles in floor
			sum += b?1:0;
		return sum;
	}

	static HashMap<Point, Boolean> buildFloor() {
		HashMap<Point, Boolean> floor = new HashMap<Point, Boolean>();
		for(String line: StringArrInput("inputs/input24.txt")) {	//for every path to a tile
			Point p = new Point(0,0);
			for(int i=0;i<line.length();i++) {	//reading directions here
				String dir = ""+line.charAt(i);	
				if("ns".contains(dir))	//if it's a two-char direction, read next char as well
					dir += line.charAt(++i);
				switch(dir) {	//move according to direction (I'm effectively moving the hexagon rows over by half, to have a 'normal' coordinate system))
				case "nw": p = p.add(new Point(0,1)); break;
				case "ne": p = p.add(new Point(1,1)); break;
				case "sw": p = p.add(new Point(-1,-1)); break;
				case "se": p = p.add(new Point(0,-1)); break;
				case "w": p = p.add(new Point(-1,0)); break;
				case "e": p = p.add(new Point(1,0)); break;
				default: println("err");
				}
			}
			floor.put(p, !floor.getOrDefault(p, false));
		}
		return floor;
	}

	static HashMap<Point, Boolean> iterate(HashMap<Point, Boolean> floor) {
		HashMap<Point, Boolean> ret = new HashMap<Point, Boolean>();
		Point[] dirs = {new Point(0,1),new Point(1,1),new Point(-1,-1),new Point(0,-1),new Point(-1,0),new Point(1,0)};
		for(Point s: floor.keySet())
			for(Point d:dirs)
				ret.put(s.add(d), floor.getOrDefault(s.add(d), false));	//add all potentially changing tiles to ret
		floor.putAll(ret);	//put those tiles back in floor
		ret.clear();
		for(Point s:floor.keySet()) {	//for every potentially changing tile
			int sum = 0;
			for(Point d:dirs)
				sum += floor.getOrDefault(s.add(d),false)?1:0;	//sum adjacent tiles if black
			if((floor.get(s) && !(sum==0||sum>2))||(!floor.get(s) && sum ==2))	//apply rules for changing tiles
				ret.put(s, true);
		}
		return ret;	//return new floor
	}
}