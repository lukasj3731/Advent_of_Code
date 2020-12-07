import java.util.HashMap;
import java.util.Map;

public class AOC07 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
	}

	static void task1() {
		String[] in = StringArrInput("inputs/input07.txt");
		Map<String, Boolean> m = new HashMap<String, Boolean>();
		for (int i = 0; i < in.length; i++)	//add shiny gold bag to map
			if (in[i].contains("shiny gold bags contain"))
				m.put(regexFinder("([a-z]* [a-z]*) ", in[i]), true);
		int curr = 0;
		do {				//while there are still bags being added
			curr = m.size();
			for (int i = 0; i < in.length; i++) {	//for every bag
				if(m.containsKey(regexFinder("([a-z]* [a-z]*)", in[i]))) {continue;}	//skip if already in map
				boolean found = false;
				for (String s : m.keySet())	//for every existing bag
					found = in[i].contains(s) ? true : found; //if existing bag in list, found = true
				if (found)
					m.put(regexFinder("([a-z]* [a-z]*) ", in[i]), true);	//add found bag
			}
		} while (curr < m.size());
		println("Task 1: " + (curr - 1));	//-1 cause shiny gold itself doesn't count
	}

	static void task2() {
		String[] in = StringArrInput("inputs/input07.txt");
		Map<String, Integer> m = new HashMap<String, Integer>();
		for (int i = 0; i < in.length; i++)	//save all empty bags with 0 contents in map
			if (in[i].contains(" no other "))
				m.put(regexFinder("([a-z]* [a-z]*) ", in[i]), 0);
		int curr = 0;
		do {	//while there are still bags being added
			curr = m.size();
			for (int i = 0; i < in.length; i++) {	//for every bag
				if(m.containsKey(regexFinder("([a-z]* [a-z]*)", in[i]))) {continue;}	//skip if already in map
				boolean allComponents = true;	
				int sum = 0;
				for (String s : in[i].split("contain")[1].split(",")) {
					allComponents = m.containsKey(regexFinder(" ([a-z]* [a-z]*)", s)) ? allComponents : false;	//see if every component exists in map
					sum += allComponents	//build sum of component bags
							? pInt(regexFinder(" ([0-9]*)", s)) * (1 + m.get(regexFinder(" ([a-z]* [a-z]*)", s))) : 0;
				}
				if (allComponents)	//if all components in map, aff current bag
					m.put(regexFinder("([a-z]* [a-z]*) ", in[i]), sum);
			}
		} while (curr < m.size());
		println("Task 2: " + m.get("shiny gold"));
	}
}