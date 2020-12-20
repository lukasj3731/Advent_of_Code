import java.util.HashMap;

public class AOC20 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}
	
	static int dimensions = 12;

	static long task1() {
		String in = StrInput("inputs/input20.txt");
		
		String[] tiles = in.split("\n\n");
		HashMap<String, Integer> m = new HashMap<String, Integer>();
		
		for(String tile:tiles) {
			String[] lines = tile.split("\n");
			String top = lines[1];
			String bottom = lines[10];
			String left = "";
			String right = "";
			for(int i=1;i<=10;i++) {
				left += lines[i].charAt(0);
				right += lines[i].charAt(9);
			}
			
			m.put(top, m.getOrDefault(top, 0)+1);
			m.put(bottom, m.getOrDefault(bottom,0)+1);
			m.put(left, m.getOrDefault(left,0)+1);
			m.put(right, m.getOrDefault(right,0)+1);
			
			top = new StringBuilder(top).reverse().toString();
			bottom = new StringBuilder(bottom).reverse().toString();
			left = new StringBuilder(left).reverse().toString();
			right = new StringBuilder(right).reverse().toString();
			
			m.put(top, m.getOrDefault(top,0)+1);
			m.put(bottom, m.getOrDefault(bottom,0)+1);
			m.put(left, m.getOrDefault(left,0)+1);
			m.put(right, m.getOrDefault(right,0)+1);
		}
		
		
		long prod = 1;
		for(String tile:tiles) {
			String[] lines = tile.split("\n");
			String top = lines[1];
			String bottom = lines[10];
			String left = "";
			String right = "";
			for(int i=1;i<=10;i++) {
				left += lines[i].charAt(0);
				right += lines[i].charAt(9);
			}
			int sum = 0;
			sum += m.get(top);
			sum += m.get(bottom);
			sum += m.get(left);
			sum += m.get(right);
			
			if(sum == 6) {
				//println("corners: "+lines[0]);
				prod *= pInt(regexFinder("Tile ([0-9]*):",lines[0]));
			}
		}
		return prod;
	}
	
	static int task2() {
String in = StrInput("inputs/input20.txt");
		
		String[] tiles = in.split("\n\n");
		HashMap<String, String> m = new HashMap<String, String>();
		
		for(String tile:tiles) {
			String[] lines = tile.split("\n");
			String top = lines[1];
			String bottom = lines[10];
			String left = "";
			String right = "";
			for(int i=1;i<=10;i++) {
				left += lines[i].charAt(0);
				right += lines[i].charAt(9);
			}
			
			m.put(top, m.getOrDefault(top, "")+","+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(bottom, m.getOrDefault(bottom,"")+","+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(left, m.getOrDefault(left,"")+","+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(right, m.getOrDefault(right,"")+","+regexFinder("Tile ([0-9]*):",lines[0]));
			
			top = new StringBuilder(top).reverse().toString();
			bottom = new StringBuilder(bottom).reverse().toString();
			left = new StringBuilder(left).reverse().toString();
			right = new StringBuilder(right).reverse().toString();
			
			m.put(top, m.getOrDefault(top,"")+",m"+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(bottom, m.getOrDefault(bottom,"")+",m"+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(left, m.getOrDefault(left,"")+",m"+regexFinder("Tile ([0-9]*):",lines[0]));
			m.put(right, m.getOrDefault(right,"")+",m"+regexFinder("Tile ([0-9]*):",lines[0]));
		}
		
		HashMap<Integer, Tile> tileMap = new HashMap<Integer, Tile>();
		
		String topLeft="";
		for(String tile:tiles) {
			String[] lines = tile.split("\n");
			String top = lines[1];
			String bottom = lines[10];
			String left = "";
			String right = "";
			for(int i=1;i<=10;i++) {
				left += lines[i].charAt(0);
				right += lines[i].charAt(9);
			}
			int sum = 0;
			sum += m.get(top).split(",").length-1;
			sum += m.get(bottom).split(",").length-1;
			sum += m.get(left).split(",").length-1;
			sum += m.get(right).split(",").length-1;
			
			if(sum == 6 && topLeft.equals("")) {
				topLeft = tile;
			}
			Tile t = new Tile(tile);
			tileMap.put(t.number, t);
		}
		
		
		
		Tile[][] map = new Tile[dimensions][dimensions];
		for(int i=0;i<map.length;i++) {
			for(int j=0;j<map.length;j++) {
				
				
				if(i==0&&j==0) {
					Tile t = new Tile(topLeft);
					t.flip();
					while(m.get(t.bottom()).split(",").length-1 != 2 || m.get(t.right()).split(",").length-1 != 2) {
						t.rotate();
					}
					map[i][j] = t;
				} else {
					if(j==0) {
						String edge = m.get(map[i-1][j].bottom()).substring(1);
						String[] tileNums = edge.replaceAll("m", "").split(",");
						Tile n;
						if(tileNums[0].equals(""+map[i-1][j].number)) {
							n = tileMap.get(pInt(tileNums[1]));
						} else {
							n = tileMap.get(pInt(tileNums[0]));
						}
						
						int r = 0;
						while(!(n.top().equals(map[i-1][j].bottom()) )) {
							if(r==4) {
								r = 0;
								n.flip();
							} else {
								n.rotate();
								r++;
							}
							//println("?1");
						}
						map[i][j] = n;
					} else {
						String edge = m.get(map[i][j-1].right()).substring(1);
						//println(map[i][j-1].right());
						//println(edge);
						String[] tileNums = edge.replaceAll("m", "").split(",");
						Tile n;
						//println(tileNums);
						if(tileNums[0].equals(""+map[i][j-1].number)) {
							n = tileMap.get(pInt(tileNums[1]));
						} else {
							n = tileMap.get(pInt(tileNums[0]));
						}
						
						int r = 0;
						while(!(n.left().equals(map[i][j-1].right()))) {
							if(r==4) {
								r = 0;
								n.flip();
							} else {
								n.rotate();
								r++;
							}
						}
						map[i][j] = n;
					}
				}
			}
		}
		
		//println("Task 1: "+topLeft);
	
		/*for(int i=0;i<map.length;i++) {
			for(int j=0;j<map.length;j++) {
				print(map[i][j].number+" ");
			}
			println("");
		}*/
		
		
		//printTiles(map);
		
		char[][] search = new char[dimensions*8][dimensions*8];
		
		for(int i=0;i<dimensions*10;i++) {
			for(int j=0;j<dimensions*10;j++) {
				if(i%10 >= 1 && i%10 <= 8 && j%10>= 1 && j%10 <= 8) {
					search[(i/10*8)+i%10-1][(j/10*8)+j%10-1] = map[i/10][j/10].map[i%10][j%10];
				}
			}
		}
		//println("");
		//println(search);
		String m1 =
				"                  # "+"\n"+
				"#    ##    ##    ###"+"\n"+
				" #  #  #  #  #  #   ";
		
		String[] m2 = m1.split("\n");
		char[][] monster = new char[m2.length][m2[0].length()];
		for(int i=0;i<m2.length;i++) {
			for(int j=0 ;j<m2[0].length();j++) {
				monster[i][j] = m2[i].charAt(j);
			}
		}
		//println(monster);
		
		int l = countMonsters(search, monster);
		
		int r = 0; 
		while(l == 0) {
			if(r==4) {
				search = flip(search);
				r = 0;
			} else {
				search = rotate(search);
				r++;
			}
			l = countMonsters(search, monster);
		}
		
		int sum = 0;
		for(int i=0;i<search.length;i++) {
			for(int j=0;j<search[0].length;j++) {
				if(search[i][j]=='#') {
					sum ++;
				}
			}
		}
		
		return sum-15*l;
	}
	
	private static int countMonsters(char[][] search, char[][] monster) {
		int sum = 0;
		for(int i=0;i<search.length-monster.length;i++) {
			for(int j=0;j<search[0].length-monster[0].length;j++) {
				
				boolean fits = true;
				for(int a=0;a<monster.length;a++) {
					for(int b=0;b<monster[0].length;b++) {
						if((search[i+a][j+b]!='#' && monster[a][b]=='#')) {
							fits = false;
						}
					}
				}
				if(fits) {
					//println("found!!"+i+","+j);
					sum ++;
				}
				
			}
		}
		return sum;
	}

	static void printTiles(Tile[][] map) {
		for(int i=0;i<dimensions*10;i++) {
			for(int j=0;j<dimensions*10;j++) {
				if(i%10==0 && j==0) {
					println("");
				}
				
				try {
					print(map[i/10][j/10].map[i%10][j%10]);
				} catch(Exception e) {
					print(" ");
				}
				if(j%10 == 9) {
					print(" ");
				}
				
			}
			println("");
		}
	}
	
	static char[][] removeBorders(char[][] tile) {
		char[][] ret = new char[tile.length-2][tile[0].length-2];
		for(int i=0;i<ret.length;i++) {
			for(int j=0;j<ret[0].length;j++) {
				ret[i][j] = tile[i+1][j+1];
			}
		}
		return ret;
	}
	
	static char[][] rotate(char[][] tile) {
		int size = tile.length;
		char[][] ret = new char[size][size];

		for (int i = 0; i < size; ++i) 
			for (int j = 0; j < size; ++j) 
				ret[i][j] = tile[size - j - 1][i];
		 return ret;
	}
	
	static char[][] flip(char[][] tile) {
		int size = tile.length;
		char[][] ret = new char[size][size];
		
		for(int i=0;i<size;i++) {
			for(int j=0;j<size;j++) {
				ret[i][j] = tile[i][size-1-j];
			}
		}
		return ret;
	}
	
	static class Tile {
		int number;
		char[][] map;
		
		public Tile(String tile) {
			String[] lines = tile.split("\n");
			number = pInt(regexFinder("Tile ([0-9]*):",lines[0]));
			map = new char[10][10];
			for(int i=0;i<10;i++) {
				for(int j=0;j<10;j++) {
					map[i][j] = lines[i+1].charAt(j);
				}
			}
		}
		
		String bottom() {
			String ret = "";
			for(int i=0;i<10;i++) {
				ret += map[9][i];
			}
			return ret;
		}
		
		String top() {
			String ret = "";
			for(int i=0;i<10;i++) {
				ret += map[0][i];
			}
			return ret;
		}
		
		String left() {
			String ret = "";
			for(int i=0;i<10;i++) {
				ret += map[i][0];
			}
			return ret;
		}
		
		String right() {
			String ret = "";
			for(int i=0;i<10;i++) {
				ret += map[i][9];
			}
			return ret;
		}
		
		void rotate() {
			int size = map.length;
			char[][] ret = new char[size][size];

			for (int i = 0; i < size; ++i) 
				for (int j = 0; j < size; ++j) 
					ret[i][j] = map[size - j - 1][i];
			map = ret;
		}
		
		void flip() {
			int size = map.length;
			char[][] ret = new char[size][size];
			
			for(int i=0;i<size;i++) {
				for(int j=0;j<size;j++) {
					ret[i][j] = map[i][size-1-j];
				}
			}
			map = ret;
		}
	}
}