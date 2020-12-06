import java.util.Arrays;
import java.util.stream.IntStream;

public class AOC06 extends AOC{	//wanted to see if i can do today in one-liners
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		println("Task 1: "+Arrays.stream(StrInput("inputs/input06.txt").split("\n\n")).mapToLong( /*for every group*/ (answers -> (Arrays.stream(answers.replaceAll("\n","").split("")).distinct().count()))).sum());	//count distinct answers and sum
	}
	
	static void task2() {
		println("Task 2: "+Arrays.stream(StrInput("inputs/input06.txt").split("\n\n")).mapToLong( /*for every group*/ answers -> IntStream.range((int)'a',((int)'z')+1).map( /*for every char*/ c -> (Arrays.stream(answers.split("\n"))).mapToInt(s -> s.contains(""+(char)c)?1:0).sum()).map( /*sum occurence of char*/ i -> (i==answers.split("\n").length?1:0)).sum()).sum());	//and save 1 if every person answered, then sum it all up
	}
}