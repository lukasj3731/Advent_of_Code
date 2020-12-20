import java.util.HashMap;

public class AOC20 extends AOC{
	public static void main(String[] args) {
		println("Task 1: "+task1());
		println("Task 2: "+task2());
	}

	static long task1() {
		long prod = 1;
		for(Tile t: getCorners(StrInput("inputs/input20.txt").split("\n\n")))
			prod *= t.number;
		return prod;
	}

	static int task2() {
		String[] tiles = StrInput("inputs/input20.txt").split("\n\n");
		HashMap<String, String> m = getMap(tiles);
		HashMap<Integer, Tile> tileMap = new HashMap<Integer, Tile>();
		for(String tile:tiles) {
			Tile t = new Tile(tile);
			tileMap.put(t.number, t);
		}
		Tile[][] map = new Tile[12][12];
		for(int i=0;i<map.length;i++)
			for(int j=0;j<map.length;j++)
				if(i==0&&j==0) {
					map[i][j] = getCorners(tiles)[0];
					while(m.get(map[i][j].dir(2)).split(",").length-1 != 2 || m.get(map[i][j].dir(1)).split(",").length-1 != 2)
						map[i][j].map=rotate(map[i][j].map);
					continue;
				} else {
					Tile t = j==0?map[i-1][j]:map[i][j-1],n;
					int dirOff = j==0?0:3,r=0;
					n = tileMap.get(pInt(m.get(t.dir(2-dirOff/3)).substring(1).replaceAll("m", "").replace(""+t.number,"").replace(",", "")));
					while(!n.dir(dirOff).equals(t.dir((2+dirOff)%4)))
						n.map=((r++)%5==4)?flip(n.map):rotate(n.map);
						map[i][j] = n;
				}
		char[][] search = new char[12*8][12*8];
		for(int i=0;i<120;i++)
			for(int j=0;j<120;j++)
				if(i%10 >= 1 && i%10 <= 8 && j%10>= 1 && j%10 <= 8)
					search[(i/10*8)+i%10-1][(j/10*8)+j%10-1] = map[i/10][j/10].map[i%10][j%10];
		char[][] monster = StrArrToCharArr("                  # \n#    ##    ##    ###\n #  #  #  #  #  #   ".split("\n"));
		int l = 0,r = 0;
		while(l == 0)
			l = countOccurrence(search = r++%5==4?flip(search):rotate(search), monster, '#');
		int sum = 0;
		for(int i=0;i<search.length;i++)
			for(int j=0;j<search[0].length;j++)
				sum += search[i][j]=='#'?1:0;
		return sum-15*l;
	}

	static HashMap<String, String> getMap(String[] tiles) {
		HashMap<String, String> m = new HashMap<String, String>();
		for(String tile:tiles) {
			Tile t = new Tile(tile);
			for(int i=0;i<4;i++) {
				m.put(t.dir(i), m.getOrDefault(t.dir(i),"")+","+t.number);
				m.put(reverse(t.dir(i)), m.getOrDefault(reverse(t.dir(i)),"")+","+t.number);
			}
		}
		return m;
	}

	static Tile[] getCorners(String[] tiles) {
		HashMap<String, String> m = getMap(tiles);
		Tile[] ret = new Tile[4];
		int index = 0;
		for(String tile:tiles) {
			Tile t = new Tile(tile);
			int sum = 0;
			for(int i=0;i<4;i++)
				sum += m.get(t.dir(i)).split(",").length-1;
			if(sum == 6)
				ret[index++]=t;
		}
		return ret;
	}

	static class Tile {
		int number;
		char[][] map;

		public Tile(String tile) {
			number = pInt(regexFinder("Tile ([0-9]*):",tile.split("\n")[0]));
			map = StrArrToCharArr(regexFinder(".*([#.\n]*)",tile).substring(1).split("\n"));
		}

		String dir(int dir) {
			String ret = "";
			for(int i=0;i<10;i++)
				ret += map[dir%2==1?i:dir*9/2][dir%2==0?i:(dir-3)*9/(-2)];
			return ret;
		}
	}
}