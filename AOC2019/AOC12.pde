int[][] input = { {-9 , 10,-1 },
                  {-14,-8 , 14},
                  { 1 , 5 , 6 },
                  {-19, 7 , 8 }};

PVector[] pos = new PVector[4];
PVector[] vel = new PVector[4];
PVector[] start = new PVector[4];
long lcm;

void setup() {
  reset();
  for (int i=0; i<1000; i++) {
    for (int j=0; j<4; j++) {
      calcGrav(j);
    }
    moveStep();
  }
  int total = 0;
  for(int i=0;i<4;i++) {
    total += getKin(i)*getPot(i);
  }
  println("Task 1: "+total);
  
  lcm = lcm(findrep(0),lcm(findrep(1),findrep(2)));
  println("Task 2: "+lcm);
}

void calcGrav(int m) {
  for (int i=0; i<4; i++) {
    PVector main = pos[m];
    PVector side = pos[i];
    vel[m].x += Integer.signum((int)(side.x-main.x));
    vel[m].y += Integer.signum((int)(side.y-main.y));
    vel[m].z += Integer.signum((int)(side.z-main.z));
  }
}

void moveStep() {
  for (int i=0; i<4; i++) {
    pos[i] = pos[i].add(vel[i]);
  }
}

int getPot(int m) {
  return (int)(abs(pos[m].x)+abs(pos[m].y)+abs(pos[m].z));
}

int getKin(int m) {
  return (int)(abs(vel[m].x)+abs(vel[m].y)+abs(vel[m].z));
}

long findrep( int a) {
  boolean running = true;
    reset();
    for (long i=0; i<Long.MAX_VALUE && running; i++) {
      for (int j=0; j<4; j++) {
        calcGrav(j);
      }
      moveStep();
      if(checkOG(a) && i>0) {
        return i+1;
      }
    }
    return Long.MAX_VALUE;
}

void reset() {
  for(int i=0;i<4;i++){
    for(int j=0;j<3;j++) {
      pos[i] = new PVector(input[i][0],input[i][1],input[i][2]);
      start[i] = new PVector(input[i][0],input[i][1],input[i][2]);
      vel[i] = new PVector(0,0,0);
    }
  }
}

long gcf(long a, long b){
    while (a != b) { 
        if (a > b) {
          a -= b;
        } else {
          b -= a;
        }
    }
    return a;
}

long lcm(long a, long b) {
    return (a * b)/gcf(a, b);
}

boolean checkOG(int a) {
  switch(a) {
    case 0: return pos[0].x == start[0].x && pos[1].x == start[1].x && pos[2].x == start[2].x && pos[3].x == start[3].x && vel[0].x == 0;
    case 1: return pos[0].y == start[0].y && pos[1].y == start[1].y && pos[2].y == start[2].y && pos[3].y == start[3].y && vel[0].y == 0;
    case 2: return pos[0].z == start[0].z && pos[1].z == start[1].z && pos[2].z == start[2].z && pos[3].z == start[3].z && vel[0].z == 0;
    default: return false;
  }
}
