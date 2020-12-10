import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class AOC10 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		List<Integer> l = Arrays.stream(intArrInput("inputs/input10.txt")).boxed().collect(Collectors.toList());
		l.add(0);
		l.sort(null);
		int one = 0,three = 1;
		for(int i=0;i<l.size()-1;i++) {
			int diff = l.get(i+1)-l.get(i);
			one += (diff==1)?1:0;
			three += (diff==3)?1:0;
		}
		println("Task 1: "+(one*three));
	}

	static void task2() {
		List<Integer> l = Arrays.stream(intArrInput("inputs/input10.txt")).boxed().collect(Collectors.toList());
		l.add(0);
		l.sort(null);
		l.add(l.get(l.size()-1)+3);
		Map<Integer, Long> m = new HashMap<Integer, Long>();
		m.put(l.get(l.size()-1), 1l);
		for(int i=l.size()-2;i>=0;i--) {
			long total = 0;
			for(int j=1;j<=3;j++)
				total += (m.containsKey(l.get(i)+j))?m.get(l.get(i)+j):0;
			m.put(l.get(i), total);
		}
		println("Task 2: "+m.get(0));
	}
}