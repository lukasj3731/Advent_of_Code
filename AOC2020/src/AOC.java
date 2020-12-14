import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class AOC {		//helpful methods to save some typing

	public static void main(String[] args){
		long start = System.currentTimeMillis();
		for(int i=1;i<=25;i++) 
			try{
				println("AOC"+String.format("%02d", i)+":");
				Class.forName("AOC"+String.format("%02d", i)).getDeclaredMethod("task1").invoke(null, (Object[]) null);
				Class.forName("AOC"+String.format("%02d", i)).getDeclaredMethod("task2").invoke(null, (Object[]) null);
				println("");
			} catch (Exception e) {} //it's fine, the event is not done yet
		println("Execution took "+(System.currentTimeMillis()-start)/1000.0+" seconds");
	}
	
	public static String StrInput(String path) {
		try {
			return new String(Files.readAllBytes(Paths.get(path)));
		} catch (IOException e) {
			e.printStackTrace();
			return "";
		}
	}

	static void println(int [][] arr) {
		Arrays.stream(arr).forEach((row) -> {println(row);});
	}

	static void println(int[] arr) {
		System.out.print("[");
		Arrays.stream(arr).forEach((el)->System.out.print(" "+el+" "));
		System.out.print("]\n");
	}
	
	static void println(char [][] arr) {
		Arrays.stream(arr).forEach((row) -> {println(row);});
	}

	static void println(char[] arr) {
		new String(arr).chars().mapToObj(i->(char)i).forEach((el)->System.out.print(el));
		System.out.println("");
	}

	static void println(Object o) {
		System.out.println(o);
	}

	static void print(Object o) {
		System.out.print(o);
	}

	static int[] intArrInput(String path) {
		return Arrays.stream(StrInput(path).split("\n")).mapToInt(Integer::parseInt).toArray();
	}

	static long[] longArrInput(String path) {
		return Arrays.stream(StrInput(path).split("\n")).mapToLong(Long::parseLong).toArray();
	}

	static double[] doubleArrInput(String path) {
		return Arrays.stream(StrInput(path).split("\n")).mapToDouble(Double::parseDouble).toArray();
	}

	static String[] StringArrInput(String path) {
		return StrInput(path).split("\n");
	}
	
	static char[][] charArrInput(String path) {
		String[] in = StringArrInput(path);
		char[][] map = new char[in.length][in[0].length()];
		for(int i=0;i<in.length;i++)
			for(int j=0;j<in[i].length();j++)
				map[i][j] = in[i].charAt(j);
		return map;
	}
	
	static List<Integer> intListInput(String path) {
		return Arrays.stream(intArrInput(path)).boxed().collect(Collectors.toList());
	}

	static int gcd(int a, int b) {
		if (b==0) return a;
		return gcd(b,a%b);
	}

	static int lcm(int a, int b) {
		return (a*b)/gcd(a, b);
	}

	static long gcd(long a, long b) {
		if (b==0) return a;
		return gcd(b,a%b);
	}

	static long lcm(long a, long b) {
		return (a*b)/gcd(a, b);
	}
	
	static int countChar(String in, char c) {
		int count = 0;
		for(int i=0;i<in.length();i++)
			count += in.charAt(i)==c?1:0;
		return count;
	}
	
	static boolean xor(boolean a, boolean b) {
		return a&&!b || b&&!a;
	}
	
	static boolean between(int a, int b, int c) {
		return a<=b && b<=c;
	}
	
	static String regexFinder(String regex, String search) {
		Pattern pattern = Pattern.compile(regex);
		Matcher matcher = pattern.matcher(search);
		return matcher.find()?matcher.group(1):"";
	}
	
	static int pInt(String in) {
		return Integer.parseInt(in);
	}
	
	static double pDouble(String in) {
		return Double.parseDouble(in);
	}
	
	static long pLong(String in) {
		return Long.parseLong(in);
	}
	
	static int binaryFromString(String in, char one) {	//turns a string of symbols into binary, where <one> indicates a 1 and any other symbol a 0
		int number=0;
		for(int i=0;i<in.length();i++)
			number=2*number+(in.charAt(i)==one?1:0);
		return number;
	}
	
	static long binaryFromStringLong(String in, char one) {	//turns a string of symbols into binary, where <one> indicates a 1 and any other symbol a 0
		long number=0;
		for(int i=0;i<in.length();i++)
			number=2*number+(in.charAt(i)==one?1:0);
		return number;
	}
	
	static boolean equal(char[][] a, char[][] b) {	//returns if 2 char arrays of same size are equal
		for(int i=0;i<a.length;i++)
			for(int j=0;j<a[i].length;j++)
				if(a[i][j] != b[i][j])
					return false;
		return true;
	}
	
	static long chineseRemainder(int[] num, int[] rem) {		//chinese remainder algo
		long product = 1, sum = 0;
		for (int i = 0; i < num.length; i++)
			product *= num[i];
		for (int i = 0; i < num.length; i++)
			sum += (product/num[i] * modInv(product/num[i],num[i]) * rem[i]);
		return sum%product;
	}
	
	static long modInv(long a, long m) {	//modular multiplicative inverse
		a = a % m; 
        for (int x = 1; x < m; x++) 
            if ((a * x) % m == 1) 
                return x; 
        return 1; 
	}
	
	static class Point{
		int x=0;
		int y=0;
		int z=0;
		int val=0;
		String name = "";
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
		
		public Point(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
		
		public Point(int x, int y, int z, int val, String name) {
			this.x = x;
			this.y = y;
			this.z = z;
			this.val = val;
			this.name = name;
			
		}
		
		public Point add(Point p) {
			return new Point(this.x + p.x,this.y + p.y,this.z + p.z, this.val + p.val, this.name +"|"+p.name);
		}
		
		public Point scale(int s) {
			return new Point(this.x*s,this.y*s,this.z*s, this.val, this.name);
		}
	}
	
	static class PointLong {
		long x=0;
		long y=0;
		long z=0;
		long val=0;
		String name = "";
		
		public PointLong(long x, long y) {
			this.x = x;
			this.y = y;
		}
		
		public PointLong(long x, long y, long z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
		
		public PointLong(long x, long y, long z, long val, String name) {
			this.x = x;
			this.y = y;
			this.z = z;
			this.val = val;
			this.name = name;
		}
		
		public void add(PointLong p) {
			this.x += p.x;
			this.y += p.y;
			this.z += p.z;
		}
	}
}
