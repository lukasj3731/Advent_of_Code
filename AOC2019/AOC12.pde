int[][] input = { {-9, 10, -1 }, 
  {-14, -8, 14}, 
  { 1, 5, 6 }, 
  {-19, 7, 8 }};

PVector[] pos = new PVector[4];
PVector[] vel = new PVector[4];
PVector[] start = new PVector[4];
long[] rep = {-1, -1, -1};

void setup() {
  simOrbit(1000);
  int total = 0;
  for (int i=0; i<4; i++) {
    total += (abs(pos[i].x)+abs(pos[i].y)+abs(pos[i].z))*(abs(vel[i].x)+abs(vel[i].y)+abs(vel[i].z));
  }
  println("Task 1: "+total);

  simOrbit(-1);
  println("Task 2: "+lcm(rep[0], lcm(rep[1], rep[2])));
}

void calcGrav() {
  for (int m=0; m<4; m++) {
    for (int i=0; i<4; i++) {
      vel[m].x += Integer.signum((int)(pos[i].x-pos[m].x));
      vel[m].y += Integer.signum((int)(pos[i].y-pos[m].y));
      vel[m].z += Integer.signum((int)(pos[i].z-pos[m].z));
    }
  }
}

void moveStep() {
  for (int i=0; i<4; i++) {
    pos[i] = pos[i].add(vel[i]);
  }
}

void simOrbit(int m) {
  long i = 0;
  reset();
  while (true) {
    calcGrav();
    moveStep();
    i++;
    for (int r =0; r<3; r++) {
      if (checkOG(r) && rep[r]==-1) {
        rep[r]=i;
      }
    }
    if ((rep[0] > 0 && rep[1] > 0 && rep[2] > 0) || i==m) {
      return;
    }
  }
}

void reset() {
  for (int i=0; i<4; i++) {
    for (int j=0; j<3; j++) {
      pos[i] = new PVector(input[i][0], input[i][1], input[i][2]);
      start[i] = new PVector(input[i][0], input[i][1], input[i][2]);
      vel[i] = new PVector(0, 0, 0);
    }
  }
}

long gcf(long a, long b) {
  if (b == 0) return a;
    else return (gcf(b, a % b));
}

long lcm(long a, long b) {
  return (a * b)/gcf(a, b);
}

boolean checkOG(int a) {
  boolean ret = true;
  for (int i=0; i<3; i++) {
    switch(a) {
    case 0: 
      ret = (pos[i].x == start[i].x && vel[i].x==0)? ret:false; 
      break;
    case 1:
      ret = (pos[i].y == start[i].y && vel[i].y==0)? ret:false; 
      break;
    case 2:
      ret = (pos[i].z == start[i].z && vel[i].z==0)? ret:false; 
      break;
    }
  }
  return ret;
}
