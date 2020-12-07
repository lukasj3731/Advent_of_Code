import java.util.HashMap;
import java.util.Map;

public class AOC07 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		String[] in = StringArrInput("inputs/input07.txt");
		Map<String, Boolean> m = new HashMap<String, Boolean>();
		for(int i=0;i<in.length;i++)
			if(in[i].contains("shiny gold bags contain")) 
				m.put(regexFinder("([a-z]* [a-z]*) ", in[i]),true);
		int curr = 0;
		int prev = -1;
		while(prev != curr) {
			for(int i=0;i<in.length;i++) {
				boolean found = false;
				for(String s:m.keySet())
					found = in[i].contains(s)?true:found;
				if (found)
					m.put(regexFinder("([a-z]* [a-z]*) ", in[i]),true);
			}
			prev = curr;
			curr = m.size();
		}
		println("Task 1: "+(curr-1));
	}
	
	static void task2() {
		String[] in = StringArrInput("inputs/input07.txt");
		Map<String, Integer> m = new HashMap<String, Integer>();
		for(int i=0;i<in.length;i++)
			if(in[i].contains(" no other "))
				m.put(regexFinder("([a-z]* [a-z]*) ", in[i]),0);
		int curr = 0;
		int prev = -1;
		while(prev != curr) {
			for(int i=0;i<in.length;i++) {
				boolean allComponents = true;
				int sum = 0;
				for(String s:in[i].split("contain")[1].split(",")) {
					allComponents = m.containsKey(regexFinder(" ([a-z]* [a-z]*)",s))?allComponents:false;
					if(allComponents)
						sum += Integer.parseInt(regexFinder(" ([0-9]*)",s)) * (1+ m.get(regexFinder(" ([a-z]* [a-z]*)",s)));
				}
				if(allComponents)
					m.put(regexFinder("([a-z]* [a-z]*) ", in[i]),sum);
			}
			prev = curr;
			curr = m.size();
		}
		println("Task 2: "+m.get("shiny gold"));
	}
}