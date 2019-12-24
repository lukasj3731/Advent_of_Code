import java.util.*;

String in = ".##..,##.#.,##.##,.#..#,#.###";

Map<Long, Boolean> rep = new HashMap<Long, Boolean>();

String[] m = in.split(",");
char[][] map1 = new char[5][5];
char[][][] map2 = new char[220][5][5];
int mid=110;

int[] dx = {0, 0, 1, -1};
int[] dy = {1, -1, 0, 0};

char[] alive = {'.', '#', '.', '.', '.', '.', '.', '.', '.'};
char[] dead =  {'.', '#', '#', '.', '.', '.', '.', '.', '.'};

void setup() {
  for (int i=0; i<map1.length; i++) {
    for (int j=0; j<map1[0].length; j++) {
      map2[mid][i][j] = m[i].charAt(j);
      map1[i][j] = m[i].charAt(j);
    }
  }
  boolean r = true;
  while (r) {
    if (rep.containsKey(calcScore(map1))) {
      println("Task 1: "+calcScore(map1));
      r = false;
    } else {
      rep.put(calcScore(map1), true);
    }
    map1 = step1();
  }
  for (int i=0; i<200; i++) {
    map2 = step2(map2);
  }
  println("Task 2: "+countAll(map2));
}

int countAll(char[][][] map) {
  int sum = 0;
  for (int a=0; a<map.length; a++) {
    for (int b=0; b<map[a].length; b++) {
      for (int c = 0; c<map[a][b].length; c++) {
        if (map[a][b][c] == '#' && !(b==2 && c==2)) {
          sum++;
        }
      }
    }
  }
  return sum;
}

char[][][] step2(char[][][] map) {
  char[][][] ret = new char[map.length][map[0].length][map[0][0].length];
  for (int d=1; d<map.length-1; d++) {
    for (int i=0; i<map[0].length; i++) {
      for (int j=0; j<map[0][0].length; j++) {
        int sum = 0;
        for (int dir=0; dir<4; dir++) {
          sum += map2(i+dx[dir], j+dy[dir], d, dir);
        }
        if (map[d][i][j]=='#') {
          ret[d][i][j] = alive[sum];
        } else {
          ret[d][i][j] = dead[sum];
        }
      }
    }
  }
  return ret;
}

long calcScore(char[][] map) {
  int index = 0;
  double sum = 0;
  for (int i=0; i<5; i++) {
    for (int j=0; j<5; j++) {
      if (map[i][j]=='#') {
        sum += pow(2, index);
      }
      index++;
    }
  }
  return (long)sum;
}

int map2(int x, int y, int depth, int dir) {
  try {
    if (x==2 && y==2) {
      int sum = 0;
      for (int i=0; i<5; i++) {
        if(dir<2) {
          sum += map2(i, (dir%2==0)?0:4, depth+1, 0);
        } else {
          sum += map2((dir%2==0)?0:4, i, depth+1, 0);
        }
      }
      return sum;
    }
    return map2[depth][x][y]=='#'?1:0;
  } 
  catch (Exception e) {
    if (x>4) {
      return map2[depth-1][3][2]=='#'?1:0;
    } else if (x<0) {
      return map2[depth-1][1][2]=='#'?1:0;
    } else if (y>4) {
      return map2[depth-1][2][3]=='#'?1:0;
    } else {
      return map2[depth-1][2][1]=='#'?1:0;
    }
  }
}

char[][] step1() {
  char[][] ret = new char[map1.length][map1[0].length];
  for (int i=0; i<5; i++) {
    for (int j=0; j<5; j++) {
      int sum = 0;
      for (int d=0; d<4; d++) {
        if (map1(i+dx[d], j+dy[d])=='#') {
          sum++;
        }
      }
      if (map1[i][j]=='#') {
        ret[i][j] = alive[sum];
      } else {
        ret[i][j] = dead[sum];
      }
    }
  }
  return ret;
}

char map1(int x, int y) {
  try {
    return map1[x][y];
  } 
  catch (Exception e) {
    return '.';
  }
}
