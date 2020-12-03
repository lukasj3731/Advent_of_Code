public class AOC01 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		int[] exp = intArrInput("inputs/input01.txt");	//read expenses
		for(int i=0;i<exp.length;i++) {
			for(int j=i+1;j<exp.length;j++) {
				if(exp[i]+exp[j]==2020)  {				//if sum to 2020, print product
					println("task 1: "+(exp[i]*exp[j]));
					return;
				}
			}
		}
	}
	
	static void task2() {
		int[] exp = intArrInput("inputs/input01.txt");	//read expenses
		for(int i=0;i<exp.length;i++) {
			for(int j=i+1;j<exp.length;j++) {
				for(int k=j+1;k<exp.length;k++){
					if(exp[i]+exp[j]+exp[k]==2020)  {	//if sum to 2020, print product
						println("task 2: "+(exp[i]*exp[j]*exp[k]));
						return;
					}
				}
			}
		}
	}
}