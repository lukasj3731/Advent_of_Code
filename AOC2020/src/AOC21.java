import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

public class AOC21 extends AOC {
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int task1() {
		HashMap<String, HashSet<String>> m = new HashMap<String, HashSet<String>>();
		HashMap<String, Integer> total = new HashMap<String, Integer>();
		fillMaps(m,total);
		for(String s:m.keySet())
			for(String i:m.get(s))
				total.remove(i);	//remove every element that could be an ingredíent
		int sum = 0;
		for(String s:total.keySet())
			sum += total.get(s);	//sum leftover elements
		return sum;
	}
	
	static String task2() {
		HashMap<String, HashSet<String>> m = new HashMap<String, HashSet<String>>();
		HashMap<String, Integer> total = new HashMap<String, Integer>();
		fillMaps(m,total);
		LinkedList<String> ingr = new LinkedList<String>();
		for(String safe = ".";!safe.equals("");) {	//loop to remove duplicates until only identifiable ingredients are left
			safe = "";
			for(String s:m.keySet())
				safe = m.get(s).size()==1?s+":"+m.get(s).iterator().next():safe;
			if(!safe.equals("")) {
				for(String s:m.keySet())
					m.get(s).remove(safe.split(":")[1]);
				ingr.add(safe);
			}
		}
		ingr.sort(null);	//sort ingredients
		return ingr.toString().replaceAll("\\[|\\]| ", "").replaceAll("([a-z]*:)","");	//remove actual ingredient name and only keep obscured name
	}
	
	static void fillMaps(HashMap<String, HashSet<String>> m ,HashMap<String, Integer> total) {	//fills map m: [allergene -> possible ingredients], total: [ingredient -> occurrence]
		for(String l: StringArrInput("inputs/input21.txt")) {
			HashSet<String> list = new HashSet<String>();
			for(String s:l.split("\\(")[0].split(" ")) {	//ingredients
				list.add(s);
				total.put(s, total.getOrDefault(s, 0)+1);
			}
			for(String a:regexFinder("\\(([^()]+)\\)", l).replaceAll("contains ", "").split(", ")) {	//allergens
				HashSet<String> tmp = m.getOrDefault(a, new HashSet<String>(list));
				tmp.retainAll(list);
				m.put(a, tmp);
			}
		}
	}
}