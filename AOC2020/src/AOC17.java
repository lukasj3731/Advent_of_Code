import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class AOC17 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		task(false);
	}

	static void task2() {
		task(true);
	}

	static void task(boolean t2) {
		char[][] in = charArrInput("inputs/input17.txt");
		Map<Point4D, Character> m = new HashMap<Point4D, Character>();
		List<Point4D> directions = new LinkedList<Point4D>();
		for (int a = -1; a <= 1; a++)
			for (int b = -1; b <= 1; b++)
				for (int c = -1; c <= 1; c++)
					for (int d = -1; d <= 1; d++)
						if (!(a == 0 && b == 0 && c == 0 && d == 0) && t2) {	//for task 2: add all valid 4d directions to map
							directions.add(new Point4D(a, b, c, d));
						} else if (!(a == 0 && b == 0 && c == 0 || d!=0) && !t2) {	//for task 1: add all valid 3d directions to map
							directions.add(new Point4D(a, b, c, 0));
						}
		for (int i = 0; i < in.length; i++)
			for (int j = 0; j < in[i].length; j++)
				m.put(new Point4D(i, j, 0, 0), in[i][j]);	//add points from input to map
		for (int i = 0; i < 6; i++)
			m = iterate(m, directions);	//iterate 6 times
		println("Task " + (t2 ? 2 : 1) + ": " + m.size());
	}
	
	static Map<Point4D, Character> iterate(Map<Point4D, Character> m, List<Point4D> directions) {
		Map<Point4D, Character> ret = new HashMap<Point4D, Character>();
		ret.putAll(m);
		for (Point4D p : ret.keySet())
			for (Point4D d : directions)
				m.putIfAbsent(p.add(d), '.');	//add all possibly reachale points to m
		ret.clear();
		for (Point4D p : m.keySet()) {	//for every point
			int sum = 0;
			for (Point4D d : directions)
				sum += m.getOrDefault(p.add(d), '.') == '#' ? 1 : 0;	//count up adjacent #
			if (sum == 3 || (sum == 2 && m.get(p) == '#'))	//and put a # to ret if conditions are met
				ret.put(p, '#');
		}
		return ret;		//return iterated map;
	}
}