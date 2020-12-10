import java.util.Arrays;
import java.util.stream.IntStream;

public class AOC06 extends AOC{	//wanted to see if i can do today in one-liners
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		println("Task 1: " + Arrays.stream(StrInput("inputs/input06.txt").split("\n\n"))
				.mapToLong((answers -> (Arrays.stream(answers.replaceAll("\n", "").split(""))
						.distinct().count()))) //for every group count distinct answers and sum
				.sum());
	}
	
	static void task2() {
		println("Task 2: " + Arrays.stream(StrInput("inputs/input06.txt").split("\n\n"))
				.mapToLong( answers -> IntStream.range((int) 'a', ((int) 'z') + 1)	//for every char in every group
						.map( c -> (Arrays.stream(answers.split("\n")))
								.mapToInt(s -> s.contains("" + (char) c) ? 1 : 0).sum())
						.map( i -> (i == answers.split("\n").length ? 1 : 0)).sum())	//sum occurrence of char
				.sum()); // and save 1 if every person answered, then sum it all up
	}
}