String in ="..#..###....#####....###........#,.##.##...#.#.......#......##....#,#..#..##.#..###...##....#......##,..####...#..##...####.#.......#.#,...#.#.....##...#.####.#.###.#..#,#..#..##.#.#.####.#.###.#.##.....,#.##...##.....##.#......#.....##.,.#..##.##.#..#....#...#...#...##.,.#..#.....###.#..##.###.##.......,.##...#..#####.#.#......####.....,..##.#.#.#.###..#...#.#..##.#....,.....#....#....##.####....#......,.#..##.#.........#..#......###..#,#.##....#.#..#.#....#.###...#....,.##...##..#.#.#...###..#.#.#..###,.#..##..##...##...#.#.#...#..#.#.,.#..#..##.##...###.##.#......#...,...#.....###.....#....#..#....#..,.#...###..#......#.##.#...#.####.,....#.##...##.#...#........#.#...,..#.##....#..#.......##.##.....#.,.#.#....###.#.#.#.#.#............,#....####.##....#..###.##.#.#..#.,......##....#.#.#...#...#..#.....,...#.#..####.##.#.........###..##,.......#....#.##.......#.#.###...,...#..#.#.........#...###......#.,.#.##.#.#.#.#........#.#.##..#...,.......#.##.#...........#..#.#...,.####....##..#..##.#.##.##..##...,.#.#..###.#..#...#....#.###.#..#.,............#...#...#.......#.#..,.........###.#.....#..##..#.##...";
String[] l;
char[][] asteroidfield;
ArrayList<Vec> vectors = new ArrayList<Vec>();
ArrayList<PVector> vecs = new ArrayList<PVector>();
Vec pos;
Vec exp200;
Vec Laser = new Vec(-1,0);

void setup() {
  l = in.split(",");
  asteroidfield = new char[l.length][l[0].length()];
  for (int i=0; i<l.length; i++) {
    for (int j=0; j<l[i].length(); j++) {
      asteroidfield[i][j] = l[i].charAt(j);
    }
  }
  int max = 0;
  for (int i=0; i<asteroidfield.length; i++) {
    for (int j=0; j<asteroidfield[0].length; j++) {
      int temp;
      if (asteroidfield[i][j]=='#' && (temp = getVisibleAsteroids(asteroidfield, i, j))>max) {
        pos = new Vec(i,j);
        max = temp;
      }
    }
  }
  println("Task 1: "+max+ " at pos: ("+(int)pos.p.y+","+(int)pos.p.x+")");
  
  ArrayList<Vec> allasteroids = getAsteroids(asteroidfield,(int)pos.p.x,(int)pos.p.y);
  int m=1;
  while(m<=200) {
    if(hitAsteroid(allasteroids, m)) {
      m++;
    }
    Laser.p.rotate(-0.001);
  }
  println("Task 2: "+(int)(exp200.p.y*100+exp200.p.x)+" at pos ("+(int)exp200.p.y+","+(int)exp200.p.x+")");
}

boolean hitAsteroid(ArrayList<Vec> allasteroids,int m) {
  Vec temp=new Vec(10000,10000);
  for(Vec v:allasteroids) {
    if(v.equals(Laser)) {
      if(temp.p.mag()>v.p.mag()) {
        temp = v;
      }
    }
  }
    if(temp.p.mag() != (new Vec(10000,10000)).p.mag()) {
      while(allasteroids.contains(temp)) {
        allasteroids.remove(temp);
      }
      if(m==200) {
        exp200 = new Vec((int)(pos.p.x+temp.p.x),(int)(pos.p.y+temp.p.y));
      }
      return true;
    }
  return false;
}

ArrayList<Vec> getAsteroids(char[][] field, int x, int y) {
  ArrayList<Vec> allasteroids = new ArrayList<Vec>();
  for (int i=0; i<field.length; i++) {
    for (int j=0; j<field[i].length; j++) {
      if ((i!=x || j!=y) && field[i][j]=='#') {
          allasteroids.add(new Vec(i-x, j-y));
      }
    }
  }
  return allasteroids;
}

int getVisibleAsteroids(char[][] field, int x, int y) {
  vectors = new ArrayList<Vec>();
  for (int i=0; i<field.length; i++) {
    for (int j=0; j<field[i].length; j++) {
      if ((i!=x || j!=y) && field[i][j]=='#') {
        Vec c = new Vec(i-x, j-y);
        if (!vectors.contains(c)) {
          vectors.add(c);
        }
      }
    }
  }
  return vectors.size();
}

class Vec {
  PVector p;

  public Vec(int a, int b) {
    p = new PVector(a, b);
  }

  boolean equals(Object o) {
    return PVector.angleBetween(p, ((Vec)o).p)<0.001;
  }
}
