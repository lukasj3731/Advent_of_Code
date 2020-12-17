public class AOC17 extends AOC{
	public static void main(String[] args) {
		task1();
		task2();
	}
	
	static void task1() {
		char[][] in = charArrInput("inputs/input17.txt");
		int iter=6;
		char[][][] map = new char[in.length+2*(iter+1)][in.length+2*(iter+1)][2*(iter+1)];
		
		for(int i=0;i<map[0][0].length;i++) {
			for(int j=0;j<map.length;j++) {
				for(int k=0;k<map[0].length;k++) {
					map[j][k][i]='.';
				}
			}
		}
		
		for(int i=0;i<in.length;i++) {
			for(int j=0;j<in[i].length;j++) {
				map[i+iter][j+iter][iter] = in[i][j];
			}
		}
		
		//print3d(map);
		
		for(int i=0;i<6;i++) 
			map = iterate(map);
		
		//print3d(map);
		
		int sum = 0;
		
		for(int i=0;i<map[0][0].length;i++) {
			for(int j=0;j<map.length;j++) {
				for(int k=0;k<map[0].length;k++) {
					if(map[j][k][i]=='#') {
						sum ++;
					}
				}
			}
		}
		
		println("Task 1: "+sum);
	}
	
	static void task2() {
		char[][] in = charArrInput("inputs/input17.txt");
		int iter=6;
		char[][][][] map = new char[in.length+2*(iter+1)][in.length+2*(iter+1)][2*(iter+1)][2*(iter+1)];
		
		for(int i=0;i<map[0][0].length;i++) {
			for(int j=0;j<map.length;j++) {
				for(int k=0;k<map[0].length;k++) {
					for(int l=0;l<map[0][0][0].length;l++) {
						map[j][k][i][l]='.';
					}
				}
			}
		}
		
		for(int i=0;i<in.length;i++) {
			for(int j=0;j<in[i].length;j++) {
				map[i+iter][j+iter][iter][iter] = in[i][j];
			}
		}
		
		//print3d(map);
		
		for(int i=0;i<6;i++) 
			map = iterate(map);
		
		
		int sum = 0;
		
		for(int i=0;i<map[0][0].length;i++) {
			for(int j=0;j<map.length;j++) {
				for(int k=0;k<map[0].length;k++) {
					for(int l=0;l<map[0][0][0].length;l++) {
						if(map[j][k][i][l]=='#') {
							sum ++;
						}
					}
				}
			}
		}
		
		println("Task 2: "+sum);
	}
	
	static char[][][] iterate(char[][][] map) {
		char[][][] ret = new char[map.length][map[0].length][map[0][0].length];
		
		for(int i=0;i<map.length;i++) {
			for(int j=0;j<map[0].length;j++) {
				for(int k=0;k<map[0][0].length;k++) {
					
					int sum = 0;

					for(int a=-1;a<=1;a++) {
						for(int b=-1;b<=1;b++) {
							for(int c=-1;c<=1;c++) {
								if(a!=0||b!=0||c!=0){
									try{
										char ch = map[i+a][j+b][k+c];
										if(ch=='#') {
											sum++;
										}
									} catch (Exception e) {
									}
								}
							}
						}
					}
					
					if(map[i][j][k]=='#') {
						if(sum ==2 || sum == 3) {
							ret[i][j][k] = '#';
						} else {
							ret[i][j][k] = '.';
						}
					} else {
						if(sum == 3) {
							ret[i][j][k] = '#';
						} else {
							ret[i][j][k] = '.';
						}
					}
					
					
					
					
					
				}
			}
		}
		return ret;
	}
	
	static char[][][][] iterate(char[][][][] map) {
		char[][][][] ret = new char[map.length][map[0].length][map[0][0].length][map[0][0][0].length];
		
		for(int i=0;i<map.length;i++) {
			for(int j=0;j<map[0].length;j++) {
				for(int k=0;k<map[0][0].length;k++) {
					for(int l=0;l<map[0][0][0].length;l++) {
					
					int sum = 0;

					for(int a=-1;a<=1;a++) {
						for(int b=-1;b<=1;b++) {
							for(int c=-1;c<=1;c++) {
								for(int d=-1;d<=1;d++) {
								if(a!=0||b!=0||c!=0||d!=0){
									try{
										char ch = map[i+a][j+b][k+c][l+d];
										if(ch=='#') {
											sum++;
										}
									} catch (Exception e) {
									}
								}
								}
							}
						}
					}
					
					if(map[i][j][k][l]=='#') {
						if(sum ==2 || sum == 3) {
							ret[i][j][k][l] = '#';
						} else {
							ret[i][j][k][l] = '.';
						}
					} else {
						if(sum == 3) {
							ret[i][j][k][l] = '#';
						} else {
							ret[i][j][k][l] = '.';
						}
					}
					
					
					
					}
					
				}
			}
		}
		return ret;
	}
}