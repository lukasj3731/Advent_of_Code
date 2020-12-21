import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

public class AOC21 extends AOC {
	public static void main(String[] args) {
		task1();
		task2();
		
	}
	
	static void task1() {
		String[] in = StringArrInput("inputs/input21.txt");
		HashMap<String, HashSet<String>> m = new HashMap<String, HashSet<String>>();
		HashMap<String, Integer> total = new HashMap<String, Integer>();
		
		for(String l: in) {
			String[] ingr = l.split("\\(")[0].split(" ");
			String[] allergens = regexFinder("\\(([^()]+)\\)", l).replaceAll("contains ", "").split(", ");
			HashSet<String> list = new HashSet<String>();
			for(String s:ingr) {
				list.add(s);
				total.put(s, total.getOrDefault(s, 0)+1);
			}
			
			for(String a:allergens) {
				if(m.containsKey(a)) {
					HashSet<String> list2 = m.get(a);
					HashSet<String> ret = new HashSet<String>();
					for(String s:list2) {
						if(list.contains(s)) {
							ret.add(s);
						}
					}
					m.put(a, ret);
				} else {
					m.put(a, list);
				}
			}
		}
		
		for(String s:m.keySet()) {
			for(String i:m.get(s)) {
				total.remove(i);
			}
		}
		
		int sum = 0;
		
		for(String s:total.keySet()) {
			sum += total.get(s);
		}
		
		
		
		
		println("Task 1: "+sum);
	}
	
	static void task2() {
		String[] in = StringArrInput("inputs/input21.txt");
		HashMap<String, HashSet<String>> m = new HashMap<String, HashSet<String>>();
		HashMap<String, Integer> total = new HashMap<String, Integer>();
		
		for(String l: in) {
			String[] ingr = l.split("\\(")[0].split(" ");
			String[] allergens = regexFinder("\\(([^()]+)\\)", l).replaceAll("contains ", "").split(", ");
			HashSet<String> list = new HashSet<String>();
			for(String s:ingr) {
				list.add(s);
				total.put(s, total.getOrDefault(s, 0)+1);
			}
			
			for(String a:allergens) {
				if(m.containsKey(a)) {
					HashSet<String> list2 = m.get(a);
					HashSet<String> ret = new HashSet<String>();
					for(String s:list2) {
						if(list.contains(s)) {
							ret.add(s);
						}
					}
					m.put(a, ret);
				} else {
					m.put(a, list);
				}
			}
		}
		
		
		
		LinkedList<String> ingr = new LinkedList<String>();
		for(int i=0;i<100;i++) {
			String safe = "";
			String name = "";
			for(String s:m.keySet()) {
				if(m.get(s).size()==1) {
					safe = m.get(s).iterator().next();
					name = s;
				}
			}
			for(String s:m.keySet()) {
				m.get(s).remove(safe);
			}
			if(!safe.equals(""))
				ingr.add(name+":"+safe);
		}
		
	
		ingr.sort(null);
		
		
		println("Task 2: "+ingr.toString().replaceAll("\\[|\\]| ", "").replaceAll("([a-z]*:)",""));
	}
}