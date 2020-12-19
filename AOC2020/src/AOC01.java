public class AOC01 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int task1() {
		int[] exp = intArrInput("inputs/input01.txt");	//read expenses
		for(int i=0;i<exp.length;i++) 
			for(int j=i+1;j<exp.length;j++) 
				if(exp[i]+exp[j]==2020)  {				//if sum to 2020, print product
					return (exp[i]*exp[j]);
				}
		return -1;
	}
	
	static int task2() {
		int[] exp = intArrInput("inputs/input01.txt");	//read expenses
		for(int i=0;i<exp.length;i++) 
			for(int j=i+1;j<exp.length;j++) 
				for(int k=j+1;k<exp.length;k++)
					if(exp[i]+exp[j]+exp[k]==2020)  {	//if sum to 2020, print product
						return (exp[i]*exp[j]*exp[k]);
					}
		return -1;
	}
}