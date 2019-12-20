import java.util.*;

String in = "                                           C   I         O     M       H             G                                       ,                                           T   F         E     C       U             C                                       ,  #########################################.###.#########.#####.#######.#############.#####################################  ,  #...................#...#.......#.#.#.#.....#.#...#.....#...#...#.....#...#.......#.#.....#.#...#.#.#...#...#.#...#...#.#  ,  #.###.#######.###.#####.#.#.#.###.#.#.#####.#.#.#.###.#.#.#.#.###.###.###.###.#.#.#.###.###.#.###.#.#.###.###.###.#.###.#  ,  #.#.#.#.#.....#...........#.#.......#.......#...#...#.#.#.#.#.#.#.#.#.#.....#.#.#.#.#...#...#.#.#.....#.#.#...#.........#  ,  ###.#.#.###.#####.#.###.#########.###.###.#.#######.#.###.#.#.#.###.#.#.#.###.#.#.#.#.#####.#.#.###.###.#.###.###.#.#.#.#  ,  #.....#...#.#.....#.#...#.#...#.....#.#.#.#.#.#...#.#.....#.#.#.#...#...#.#.#.#.#.#...#...#...#...#...#.#.#.#.#.#.#.#.#.#  ,  #.#######.###############.#.#####.###.#.#.###.#.#.#.###.###.#.###.#.###.###.#.#.#.#.###.###.#####.#.###.#.#.#.#.#.#.#.###  ,  #.#...........#.#.#...#.................#.#.#...#.....#.#.#.#.....#.#.....#...#.#.#.#.......#.#.#.#.#.#...........#.#...#  ,  #############.#.#.###.###.#.#.###.#####.###.#.#####.#####.#.###.###.#.#.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.###.###.#.###.#  ,  #.#.....#.#.#.............#.#.#...#.....#.#.....#...#...#...#.#.#...#.#.#.#.#.#.#...........#.#.#.#.....#...#...#.#.#...#  ,  #.###.#.#.#.#.#.###.###.###.#######.#.###.###.#######.#.#.#.#.###.#######.###.###.#.###.###.#.#.#.#.###.#############.#.#  ,  #...#.#.#.....#.#.#.#...#.#.#.#.....#.....#.#.....#...#...#.....#...#.....#.#.#.#.#.#...#.............#.......#...#.#.#.#  ,  ###.#.#####.#.###.#.#.#.#.###.#.#######.###.#.#######.###.###.###.#.#.#####.#.#.###.#.###.#.###.#.#.#.###.#####.###.###.#  ,  #...........#...#...#.#.#.#...#.#.....#.....#...#...#.#.....#.#...#.#.......#.....#.#...#.#.#.#.#.#.#...#.............#.#  ,  #.#.#######.#.#.###.###.#.###.###.###.#####.#.###.###.#.#.#########.#.#.#.#.###.###.#.#######.#.#.###########.###########  ,  #.#.#.#.#...#.#.#.....#.#...#.....#.#.#.....#...#...#.#.#.#.#.#.#.#.#.#.#.#.#.....#.#.......#...#.......#...#...#.......#  ,  #.###.#.#.###.#######.#####.#######.#.#.#####.#####.#.#####.#.#.#.#.###.###.#.#.###.#############.###.###.#######.#######  ,  #.#.....#.#.#.....#...#.............#...#.#...#.#.....#.......#.#.#...#.#.#.#.#...#.....#.....#...#...#...#...#.#.#.#...#  ,  #.###.#.###.#.#####.###.###########.#.###.###.#.#####.#.###.#.#.#.#.###.#.#.#.#######.###.###############.#.#.#.#.#.#.#.#  ,  #.#.#.#.....#.#...#.#.#.#.......#...........#.......#...#.#.#.#.......#.#...#.....#.#.#...#.#.........#.....#.#.....#.#.#  ,  ###.###.###.#.#.#####.#########.#.#.#.#.#####.#.###.#.#.#.#####.#.#######.#.###.###.#####.#.###.#########.#######.###.#.#  ,  #.....#.#.#.#.#...#...............#.#.#.....#.#.#.#.#.#.......#.#.....#...#...#.....#.......#.#...#...#.......#.#.....#.#  ,  ###.###.#.#####.###.#.###.#.#.###.#.###.#####.###.#####.###.#.###.#.###.###.#.#.#.###.#.#.#.#.#.#.#.###.#######.#.#.#####  ,  #...#...#...#...#.#.#...#.#.#...#.#.#.....#.#...#...#...#...#.#...#.#.#.#...#.#.#...#.#.#.#.#...#.#.#...#...#...#.#.#...#  ,  ###.###.#.#####.#.#####################.#.#.###.#.#########.#######.#.###.#######.#.#.#####.#.#.###.###.###.###.#.#.###.#  ,  #.#.....#.#.#.........#...........#.....#.#...#.#.#...#.#.#...#...#...#...#.....#.#.#...#.....#.#...#.......#.#...#.#.#.#  ,  #.#####.#.#.#####.###########.###.###.###.###.#.#.#.###.#.#.###.#.#.###.#.###.#####.#.#.#####.#####.#.#######.#.#####.#.#  ,  #...#.......#.#...#.#.....#...#.....#...#...#.....#.......#...#.#...#.#.#.#...........#...#.#.#.......#.#.#...#.....#...#  ,  #.#######.###.###.#.#####.#####.###.#.#######.###.###.###.#.###.###.#.###.###.#########.#.#.#######.###.#.#.#####.###.###  ,  #.#...#.#.......#.#.#.#...#.#...#.......#.#...#...#...#.#.#.#...#.#.#...#...#.........#.#.#.#.#.#.#.#.......#.#.....#...#  ,  #.###.#.#.#######.#.#.#.###.#########.###.###.#######.#.#.#.#.###.###.#.###.###.#.#.#######.#.#.#.#.#.#######.#####.#.###  ,  #...........#.#.....#.....#.....#...........#...#.......#...#.......#.#.......#.#.#...#...#.......#.#.....#.#.#.........#  ,  #.#####.#.#.#.###.#.#.#.###.###.#########.#####.#####.###########.###.#########.#########.#.#######.###.###.#.#####.#####  ,  #.#.#.#.#.#.#.#.#.#...#.#...#...#        G     N     H           Q   I         H        #...#...#.#.#.....#.#.#...#.#.#.#  ,  ###.#.###.###.#.#####.#########.#        C     W     L           B   F         U        #.#####.#.#.###.###.#.#.###.#.#.#  ,  #...#...#...#.#.#.#.#...#.#...#.#                                                       #...#.......#...................#  ,  #.###.###.###.#.#.#.#.#.#.###.#.#                                                       #.#.#.#####.#.###.###.#.#.###.###  ,  #.#.#...#...#.....#.#.#.#...#...#                                                     IH..#...#.#...#.#.#...#.#.#...#...#  ,  #.#.#.###.#.###.###.###.#.###.###                                                       #.#.#.#.###.#.#.#######.#######.#  ,  #.......#.#.......#.#...........#                                                       #.#.#.#.#.....#.#.#.#...#.#.#....WD,  #.#.#########.#.###.#####.#.#####                                                       #######.#######.#.#.###.#.#.#####  ,  #.#.....#...#.#.#.#...#.#.#...#.#                                                       #.#.#...#.............#.#.#.#...#  ,  #.#.#####.#.#.#.#.#.###.#.###.#.#                                                       #.#.#.#.#.###.#.###.#.###.#.#.#.#  ,UQ..#.....#.#...#...#.#.#.....#....XT                                                   UZ....#.#.....#.#...#.#.......#.#.#  ,  ###.###.#.###.#.#.#.#.#####.#.###                                                       ###.#.###.#.###.#.#.#######.#.#.#  ,  #.#.#.....#.#.#.#...........#.#.#                                                       #...#.#.#.#.#...#.#.#.#.....#.#..AH,  #.###.#####.#####.#.#.#########.#                                                       #.###.#.#######.#####.#####.#.###  ,YI....#.#.#.#.....#.#.#.#..........RV                                                     #...........#.#.#...#.....#...#.#  ,  ###.###.#.#.#######.###.#####.###                                                       #########.###.###.#####.#.#####.#  ,  #.....#.......#...#.#...#.......#                                                       #.......#.#...#.#...#.#.#.....#..OS,  ###.#.#####.###.#########.###.#.#                                                       #.#####.#####.#.#.#.#.###.###.#.#  ,  #...#.#.#.......#.#.....#...#.#.#                                                       #.#.......#.....#.#.#.....#...#.#  ,  #.#.###.###.#.#.#.#.###.###.###.#                                                       #.#.#########.#####.#####.#.###.#  ,  #.#.........#.#.....#.#.....#...#                                                       #.#...#.#.....#.#.#.#.#.#.#.#...#  ,  #######.#######.###.#.#.###.#####                                                       #.###.#.#####.#.#.#.#.#.#.#.###.#  ,  #.....#.#...#...#.#.#.....#.#....ZO                                                   AH..#.#.....................#.....#  ,  #.#.#####.#######.###.#.###.###.#                                                       ###.#.#######################.###  ,UZ..#...#.....#.#.#.#.#.#...#.#.#.#                                                     UP..#.#...#.#.............#.#.#.#.#  ,  ###.###.###.#.#.#.#.#########.#.#                                                       #.#.#.###.###.###.###.#.#.#.###.#  ,  #.....#...#.......#...#.#.....#.#                                                       #...#.#...#.....#...#.#.......#..KD,  #.#######.#.#.#.#.#.#.#.###.###.#                                                       #.#####.#.###.#.###.#######.###.#  ,  #.........#.#.#.#...#...........#                                                       #.......#.#...#.#.....#.#.....#.#  ,  ###.###.#######.#.###.#.#########                                                       ###.#.#######.###.#####.#####.#.#  ,  #.....#.#...#.#.#...#.#.#.#...#.#                                                       #.#.#.........#.#.#.....#.......#  ,  ###########.#.###########.#.#.#.#                                                       #.#############.###.###.#######.#  ,  #.#.#.#.#.....#.#.#.....#...#...#                                                     YI....#...........#.....#.#.#.#...#  ,  #.#.#.#.###.#.#.#.###.###.###.#.#                                                       ###.#.###.###.#.#.#.#.###.#.#####  ,  #.........#.#.#.#.......#...#.#.#                                                       #...#.#.....#.#...#.#.....#.....#  ,  #.#####.###.###.#####.#.###.#.###                                                       #.#.#.#####.#.#########.###.#.###  ,MI......#...............#.....#....KD                                                     #.#.#.#.#.#.#.#...#.#.....#.#.#..ZZ,  #.#######################.#######                                                       #.###.#.#.#######.#.###.#.###.#.#  ,  #.....#...#...........#.#.#.....#                                                       #.....#.....#.#.#...#.#.#........ZO,  #.#####.#.#.#.#.#.#.#.#.###.###.#                                                       #.#####.###.#.#.#.###.###########  ,  #.#.#.#.#...#.#.#.#.#.....#...#..CT                                                     #.#.#.....#.#.........#.........#  ,  ###.#.#.#####.###########.#.#.###                                                       ###.#.#.#.###.#######.###.#.#.###  ,UP......#...#.#.....#.#.....#.#....NG                                                     #...#.#.#.......#.........#.#...#  ,  #.#.#.#.#.#.###.###.#.#########.#                                                       #.#.#.#.#####.#########.#.#####.#  ,VH..#.#...#.#...#.#...#...........#                                                       #.#.#.#.....#.....#.....#...#...#  ,  #.#########.#######.#########.###                                                       #.#.#####.###.###.#.#.#.#######.#  ,  #...#.......#.#...#...#...#...#.#                                                     VO..#.......#...#...#.#.#.#...#....IH,  #####.#####.#.###.#.#.#.#.###.#.#                                                       #.#########################.#####  ,AA....#.#...#...#.#...#...#.#.#.#.#                                                       #.#.#...#...............#........VO,  ###.#.###.#.###.###.#####.#.#.#.#                                                       ###.#.#.#.###.#.###.###.#.#.###.#  ,NW....#.....#.#.#.#.#...#.#...#.#..MI                                                   IU..#...#...#...#...#.#.....#...#.#  ,  #.#######.#.#.#.#.###.#.###.###.#                                                       #.###.#.#######.#######.###.#.###  ,  #.........#...........#.........#                                                       #...#.#.......#.#.........#.#...#  ,  #.#.#####.###.#.#.###.###.###.###                                                       #.#.#.#########.###.###.#####.###  ,  #.#...#...#.#.#.#...#.#.#.#.#...#                                                       #.#.........#...#.#.#.......#...#  ,  #.#.###.###.#.#.###.#.#.#.#.#.###      V         N M     O       O     W         U      #.#.#.#.###.#####.#.#######.#####  ,  #.#.#.......#.#...#.#...#...#...#      H         B C     S       E     D         Q      #.#.#.#...#.....#.........#.....#  ,  #.###.#.#.#####.#####.#.#####.#.#######.#########.#.#####.#######.#####.#########.###########.###########.#.#####.#.#.#.#  ,  #...#.#.#.#.....#.....#.#.....#.#.#.....#.........#.#.......#.....#.#.#.....#...#.#.......#.....#.....#.#.#.#.#.#.#.#.#.#  ,  #.#.#.#.#######.#######.###.#.###.#.###.###.###.###.#.#.#######.###.#.###.#####.#.#######.#.###.#.#####.###.#.#.###.###.#  ,  #.#.#.#.#.#.#.......#.....#.#...#.....#.#.....#.#...#.#.#...#.........#...#.....#.....#.....#.....#.#.....#.......#...#.#  ,  #.#.#.###.#.###.#######.###########.#########.#####.###.###.#########.###.###.#####.#####.#.#.#.#.#.#.#.#.#####.#####.#.#  ,  #.#.#.#.............#.....#.......#.#.....#...#...#...#.......#.........#.......#.....#...#.#.#.#.#...#.#...#.....#.#.#.#  ,  #.#.###.#.#.#####.#####.#.#######.#.#.#.###.#.###.###.###.#####.###.#.#######.###.###############.#.#.###.#####.###.###.#  ,  #.#...#.#.#.#.#.#.#.#...#...#...#...#.#...#.#.......#.#.......#...#.#.#.....#.#.......#.......#.....#...#.#.......#.....#  ,  #.#.###.#.###.#.#.#.###.#####.#####.#.#.#########.###.#######.#.#######.###.#.#####.#####.#.#####.#.#.#########.#.#####.#  ,  #.#.#.#.#.#.........#.....#.........#.#...#.......#.....#.#.#.#.....#...#.....#.#.#.......#.#.....#.#...#.#.#...#.#.....#  ,  #.###.###.###.###.#########.#.###.#.#.###.###.###.#.#####.#.#.#.#######.###.###.#.###.###.#####.#.#######.#.#########.#.#  ,  #.......#.#.#.#.#...#...#.#.#.#...#.#.#.#.#.....#.#...#.#.....#...#.#.#.#...#...#.....#.....#...#...............#.....#.#  ,  #.#.#######.#.#.###.#.#.#.#########.#.#.#.###.###.###.#.###.#.#.#.#.#.#.#####.#####.#.#####.#.#.###.#####.###.#.#######.#  ,  #.#...#...........#.#.#.#...#...........#...#...#.#...#.#...#.#.#...#.#...#.........#...#...#.#...#.....#.#.#.#.....#...#  ,  #.#.#.#.#.#.#.#.#######.###.#.#.#.###.#.#.#######.#.###.#####.#.#####.#.#######.#.###.###.#####.###.###.###.###.#.###.###  ,  #.#.#.#.#.#.#.#.#.#.#.........#.#.#.#.#.#...#...#.#.......#.#.#.#...#...#...#.#.#.#.#...#.#.......#.#.........#.#...#...#  ,  #.#.#######.#.###.#.###.###########.#.#.#.#####.#.###.#####.#.#.###.###.#.###.#.###.###.#.#####.#.###.#.#.#.#############  ,  #.#.#.....#.#.#.....#...#...#...#.#.#.#.#...#.....#.....#.#...#.......#...#.#.......#.#.#.#.....#...#.#.#.#...#.........#  ,  ###.#####.#########.#######.###.#.#.#####.###.#.###.#####.###.#.#.#####.###.###.#####.#########.#.#####.###.#.#####.###.#  ,  #.#.#.........#.#...#.#...............#.#.#.#.#...#.....#.#.#.#.#.#.......#.....#...........#...#.#.......#.#.#.#.....#.#  ,  #.#.#######.###.###.#.#####.#.#.#.#.###.#.#.#####.#.###.#.#.#.#.#####.#.#######.#.#####.#######.#####.#.###.###.#.#.#####  ,  #...#.....#.#...#.#.....#.#.#.#.#.#.#.......#.....#.#.#.#.....#...#...#...#.........#.#.#.#.#.#.....#.#...#.......#.#...#  ,  #.#.###.###.#.###.###.###.#######.###.###########.#.#.###.#.###.#######.#######.#.###.###.#.#.#################.#.#.#.#.#  ,  #.#.#.....#.#.#.#.#...#.#.#.......#...........#.#.#...#...#...#.#...#...#.....#.#.#...........#.............#...#.#...#.#  ,  #.#.###.#.#.#.#.#.###.#.#.###.###.#######.#.###.#.###.###.#.#.#.###.###.###.#.#.#.#.#######.#.#.###.###.#.#####.#.###.###  ,  #.#.#.#.#.........#...#.#.#...#.#.........#...#.....#.#...#.#.#.......#.....#.#.#.#...#...#.#.....#...#.#.#.....#.#.....#  ,  #.###.#####.#####.###.#.#.#.###.###.###.#.#######.###.#.#######.#####.#.#####.#.###.#####.###.#.#.#######.###.#######.#.#  ,  #.#.......#.#...............#.........#.#.#.........#.#...#...#.#.#...#.#.....#.#.....#.#.#.#.#.#.....#...#.........#.#.#  ,  #########.#######.#.#.###.#.###.#.#.#########.#######.###.#.###.#.###.###.#####.###.###.#.#.#####.#.#####.#####.#.#.###.#  ,  #.#.#.#.#.#...#.#.#.#.#...#...#.#.#.........#.......#...#.#...#.....#.#.....#.......#...#...#.#.#.#...#.#...#...#.#...#.#  ,  #.#.#.#.#.###.#.#.#.###.#######.#######.#####.###.###.###.#.#######.###.###########.###.#.#.#.#.#.#.###.#######.###.#####  ,  #.................#...#.....#...#.........#.....#.#...#.....#.........#.........#.........#.....#.#...........#...#.....#  ,  #####################################.###########.###.#####.###.#########.#########.#####################################  ,                                       N           I   R     H   N         X         Q                                       ,                                       B           U   V     L   G         T         B                                       ";

String[] inp = in.split(",");
String[][] map = new String[inp.length][inp[0].length()];

int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};
int DEPTH = 10000;
int task = 2;

void setup() {
  for (int i=0; i<map.length; i++) {
    for (int j=0; j<map[i].length; j++) {
      map[i][j] = ""+inp[i].charAt(j);
    }
  }

  for (int i=1; i<map.length-1; i++) {
    for (int j=1; j<map[i].length-1; j++) {
      char c = inp[i].charAt(j);
      if (c >= 'A' && c <= 'Z') {
        for (int d=0; d<4; d++) {
          if (map[i+dx[d]][j+dy[d]].charAt(0) >= 'A' && map[i+dx[d]][j+dy[d]].charAt(0) <= 'Z') {
            for (int d2=0; d2<4; d2++) {
              if (map[i+dx[d2]][j+dy[d2]].charAt(0) == '.') {
                char[] chars = (""+map[i][j]+map[i+dx[d]][j+dy[d]]).toCharArray();
                Arrays.sort(chars);
                map[i][j] = new String(chars);
                map[i+dx[d]][j+dy[d]] = " ";
              }
            }
          }
        }
      }
    }
  }
  Point start = getPositions("AA").get(0);
  Point end = getPositions("ZZ").get(0);
  map[end.x][end.y] = ".";
  task = 1;
  println("Task 1: "+getDist(start, end));
  task = 2;
  println("Task 2: "+getDist(start, end));
}



int getDist(Point start, Point end) {
  boolean[][][] visited = new boolean[map.length][map[0].length][DEPTH];
  Queue<queueNode> q = new LinkedList<queueNode>();
  queueNode s = new queueNode(start, 0, 0);
  q.add(s);

  while (!q.isEmpty()) {
    queueNode curr = q.peek();
    Point pt = curr.pt;

    if (pt.x == end.x && pt.y == end.y && pt.d == end.d) {
      return curr.dist-curr.portals-2;
    }
    q.remove();
    for (int i=0; i<4; i++) {
      Point n = new Point(pt.x + dx[i], pt.y + dy[i], curr.pt.d);
      Point afterp = goThroughPortal(n);
      
      if (isWall(n) || afterp.d <0 || visited[afterp.x][afterp.y][afterp.d]) {
        continue;
      }
      visited[afterp.x][afterp.y][afterp.d] = true;
      queueNode nextCell = new queueNode(afterp, curr.dist+1, curr.portals + (n.equals(afterp)?0:1));
      q.add(nextCell);
    }
  }
  return -1;
}

boolean isWall(Point p) {
  try {
    return (p.d < 0 || map[p.x][p.y].equals("#") || map[p.x][p.y].equals(" ") || map[p.x][p.y].equals("AA") || map[p.x][p.y].equals("ZZ"));
  } catch (Exception e) {
    return true;
  }
}

Point goThroughPortal(Point p) {
  if (map[p.x][p.y].length()==1) {
    return p;
  } else {
    ArrayList<Point> points = getPositions(map[p.x][p.y]);
    if (points.size()<2) {
      return p;
    }
    if (points.get(0).equals(p)) {
      Point tmp = points.get(1);
      if (p.d+portalAdjustLevel(p)<0 && p.d == 0) {
        return p;
      }
      return new Point(tmp.x, tmp.y, p.d+portalAdjustLevel(p));
    } else {
      Point tmp = points.get(0);
      if (p.d+portalAdjustLevel(p)<0 && p.d == 0) {
        return p;
      }
      return new Point(tmp.x, tmp.y, p.d+portalAdjustLevel(p));
    }
  }
}

int portalAdjustLevel(Point p) {
  if (task == 1) {
    return 0;
  }
  if (p.x<3 || p.x > map.length-3 || p.y < 3 || p.y>map[0].length-3) {
    return -1;
  }
  return 1;
}

ArrayList<Point> getPositions(String in) {
  ArrayList<Point> ret = new ArrayList<Point>();
  for (int i=0; i<map.length; i++) {
    for (int j=0; j<map[i].length; j++) {
      if (map[i][j].equals(in)) {
        ret.add(new Point(i, j));
      }
    }
  }

  return ret;
}

class Point { 
  int x; 
  int y; 
  int d = 0;
  char val = '_';

  public Point(int x, int y) { 
    this.x = x; 
    this.y = y;
  }

  public Point(int x, int y, char val) { 
    this.x = x; 
    this.y = y;
    this.val = val;
  }

  public Point(int x, int y, int d) { 
    this.x = x; 
    this.y = y;
    this.d = d;
  }

  String toString() {
    return "["+x+","+y+","+d+"]"+((val == '_')?"":""+val);
  }

  boolean equals(Object o) {
    Point p = (Point)o;
    return x==p.x && y==p.y;
  }
}

class queueNode 
{ 
  Point pt; // The cordinates of a cell 
  int dist; // cell's distance of from the source 
  int portals = 0;

  public queueNode(Point pt, int dist, int portals) 
  { 
    this.pt = pt; 
    this.dist = dist;
    this.portals = portals;
  }
}
