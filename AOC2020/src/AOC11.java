public class AOC11 extends AOC{
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
		char[][] prev, curr=charArrInput("inputs/input11.txt");
		do {
			prev = curr;
			curr = iterate(curr, t2);
		} while(!equal(prev,curr));		//while not identical, iterate
		int count = 0;
		for(int i=0;i<curr.length;i++)
			for(int j=0;j<curr[i].length;j++)
				count += curr[i][j]=='#'?1:0;	//count taken spaces
		println("Task "+(t2?2:1)+": "+count);
	}

	static char[][] iterate(char[][] in, boolean t2) {
		char[][] ret = new char[in.length][in[0].length];
		for(int i=0;i<in.length;i++)	//for every char in array
			for(int j=0;j<in[i].length;j++) {
				int adj = 0;
				for(int a=-1;a<=1;a++)	//for every direction
					for(int b = -1;b<=1;b++) {
						int d=1;
						char ch='.';
						while((t2 || d==1) && ch=='.' && !(a==0&&b==0) &&	//if inside array: for task1: go one step, for task 2: go till char != '.'
								between(0,i+d*a,in.length-1) && between(0,j+d*b,in[0].length-1))
							ch = in[i+d*a][j+d++*b];
						adj += (ch=='#')?1:0;	//add up adjacent '#'
					}
				ret[i][j] = (in[i][j]== 'L' && adj == 0)?'#':(	//apply rules
						in[i][j] == '#' && adj >= (t2?5:4)?'L':in[i][j]);
			}
		return ret;
	}
}