import java.util.HashMap;

public class AOC24 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		String[] in = StringArrInput("inputs/input24.txt");
		HashMap<String, Boolean> floor = new HashMap<String, Boolean>();
		
		for(String line: in) {
			Point p = new Point(0,0);
			for(int i=0;i<line.length();i++) {
				String dir = ""+line.charAt(i);
				if("ns".contains(dir)) {
					i++;
					dir += line.charAt(i);
				}
				switch(dir) {
				case "nw": p = p.add(new Point(0,1)); break;
				case "ne": p = p.add(new Point(1,1)); break;
				case "sw": p = p.add(new Point(-1,-1)); break;
				case "se": p = p.add(new Point(0,-1)); break;
				case "w": p = p.add(new Point(-1,0)); break;
				case "e": p = p.add(new Point(1,0)); break;
					default: println("err");
				}
			}
			floor.put(""+p, !floor.getOrDefault(""+p, false));
		}
		int sum =0;
		for(boolean b:floor.values()) {
			if(b) {
				sum ++;
			}
		}
		
		println("Task 1: "+sum);
	}
	
	static void task2() {
		String[] in = StringArrInput("inputs/input24.txt");
		HashMap<Point, Boolean> floor = new HashMap<Point, Boolean>();
		
		for(String line: in) {
			Point p = new Point(0,0);
			for(int i=0;i<line.length();i++) {
				String dir = ""+line.charAt(i);
				if("ns".contains(dir)) {
					i++;
					dir += line.charAt(i);
				}
				switch(dir) {
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
		for(int i=0;i<100;i++) {
		
		floor = iterate(floor);
		int sum =0;
		for(boolean b:floor.values()) {
			if(b) {
				sum ++;
			}
		}
		
		//println(i+" : "+sum);
		}
		
		int sum =0;
		for(boolean b:floor.values()) {
			if(b) {
				sum ++;
			}
		}
		println("Task 2: "+sum);
	}
	
	static HashMap<Point, Boolean> iterate(HashMap<Point, Boolean> floor) {
		HashMap<Point, Boolean> ret = new HashMap<Point, Boolean>();
		Point[] dirs = {new Point(0,1),new Point(1,1),new Point(-1,-1),new Point(0,-1),new Point(-1,0),new Point(1,0)};
		for(Point s: floor.keySet()) {
			for(Point d:dirs) {
				ret.put(s.add(d), floor.getOrDefault(s.add(d), false));
			}
		}
		for(Point p:ret.keySet()) {
			floor.put(p, ret.get(p));
		}
		ret = new HashMap<Point, Boolean>();
		
		for(Point s:floor.keySet()) {
			int sum = 0;
			for(Point d:dirs) {
				if(floor.getOrDefault(s.add(d),false)) {
					sum ++;
				}
			}
			if(floor.get(s)) {
				if(sum==0||sum>2) {
					
				} else {
					ret.put(s, true);
				}
			} else {
				if(sum ==2) {
					ret.put(s, true);
				} 
			}
		}
		
		
		return ret;
	}
}



