import java.util.*;

String s = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1001,1034,0,1039,1001,1036,0,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,1002,1036,1,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1002,1035,1,1040,1001,1038,0,1043,1002,1037,1,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1002,1035,1,1040,101,0,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,35,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,44,1044,1106,0,224,1102,0,1,1044,1106,0,224,1006,1044,247,1001,1039,0,1034,1002,1040,1,1035,102,1,1041,1036,101,0,1043,1038,1001,1042,0,1037,4,1044,1106,0,0,9,21,23,46,38,21,77,24,34,41,9,82,3,32,97,21,67,23,67,35,41,27,93,13,82,38,74,16,91,25,34,64,47,43,50,15,81,21,30,27,63,88,9,98,95,42,69,23,57,15,52,22,65,43,7,36,90,13,8,83,68,37,6,48,22,53,21,87,86,77,23,14,56,40,32,77,15,9,70,2,28,88,35,37,98,91,29,84,4,62,75,99,40,57,68,35,79,47,78,41,88,20,92,24,76,8,8,51,16,21,75,97,15,71,34,21,77,26,5,98,92,13,94,36,39,61,78,19,96,12,28,3,68,17,8,83,29,50,10,17,46,9,18,56,2,75,53,47,12,66,18,62,67,10,73,35,69,33,58,39,24,68,17,90,77,35,83,22,98,46,6,46,41,45,69,33,12,70,21,47,13,25,54,36,53,23,83,6,31,33,79,55,29,55,42,9,53,25,29,66,60,83,37,9,56,35,2,28,50,84,92,1,50,40,1,59,93,5,85,82,31,74,34,70,28,37,51,50,31,24,83,62,36,29,16,9,93,49,40,13,50,51,54,23,66,88,46,15,31,90,10,59,38,87,36,32,54,71,35,6,24,43,76,53,17,60,41,64,66,12,5,84,22,47,24,94,39,40,51,20,33,61,35,10,9,97,8,79,56,19,59,41,91,67,9,12,70,55,78,78,31,25,45,3,62,10,87,20,17,54,66,14,28,58,3,12,94,80,4,93,93,18,70,92,7,43,30,99,21,81,68,23,19,75,49,42,37,72,14,17,16,50,77,12,33,92,84,26,83,35,52,32,53,5,49,3,94,72,39,51,41,64,4,99,77,67,30,60,52,4,1,75,96,10,12,54,58,4,66,62,84,38,2,46,83,12,33,99,17,3,42,64,84,38,62,6,72,42,20,82,30,36,63,27,75,11,65,16,36,79,9,58,33,48,56,20,11,13,41,65,28,99,15,31,56,89,26,58,5,13,93,24,11,4,25,49,83,96,15,93,60,2,8,86,76,10,41,60,53,13,45,70,33,35,88,38,76,75,26,88,73,52,19,32,88,17,65,35,23,3,74,93,40,77,19,10,57,1,53,12,84,32,39,96,16,55,38,77,52,24,1,58,5,90,88,33,78,36,16,61,22,36,76,64,23,38,56,18,67,32,86,53,21,76,52,34,57,4,19,1,74,67,9,61,80,9,35,31,80,12,97,28,41,72,24,38,64,25,87,21,54,15,84,55,9,33,16,52,51,37,79,43,54,20,98,33,45,89,18,25,33,9,12,52,27,67,62,92,27,95,35,47,13,52,22,63,51,19,50,50,40,19,90,13,67,49,18,83,6,58,9,62,16,74,20,16,51,56,90,36,50,3,48,26,50,31,24,74,83,73,10,55,90,83,4,1,46,21,88,26,56,35,10,77,2,40,90,14,68,27,62,38,6,61,66,10,8,72,35,79,74,38,76,46,43,83,25,25,75,11,18,74,18,3,59,94,22,42,79,85,9,10,26,78,27,13,94,28,57,25,19,59,1,89,54,84,41,9,71,6,30,73,29,58,87,43,61,17,66,9,69,23,58,36,11,45,86,45,28,62,97,6,31,19,99,65,36,58,36,45,3,26,27,33,46,75,19,97,24,65,75,33,15,21,83,98,38,29,77,83,15,62,7,51,86,12,11,37,7,86,9,80,37,92,28,50,52,69,16,55,76,59,9,85,30,97,69,93,13,63,4,74,80,88,31,80,36,51,40,98,95,83,23,92,7,91,63,68,40,73,0,0,21,21,1,10,1,0,0,0,0,0,0";

PVector[] direc = { 
  new PVector(0, 0), 
  new PVector(0, -1), 
  new PVector(0, 1), 
  new PVector(-1, 0), 
  new PVector(1, 0)};

int task1 = 0;
int task2 = 0;
PVector start = new PVector(50, 50);
PVector goal = null;
VM droid = new VM(s);
int[][] map = new int[100][100];

void setup() {
  droid.run();
  for (int i=0; i<100; i++) {
    Arrays.fill(map[i], -1);
  }
  search();
  
  start = new PVector(50, 50);
  int[][] dis = new int[100][100];
  for (int i=0; i<100; i++) {
    Arrays.fill(dis[i], -1);
  }
  dis[(int)goal.y][(int)goal.x] = 0;
  Queue<PVector>search=new LinkedList<PVector>();
  search.add(new PVector(goal.x, goal.y));
  while (!search.isEmpty()) {
    PVector t = search.poll();
    int d = dis[(int)t.y][(int)t.x];
    if (t.x == start.x && t.y == start.y) {
      task1 = d;
    }
    task2 = max(task2, d);
    for (int dir=1; dir<=4; dir++) {
      if (map[(int)(t.y+direc[dir].y)][(int)(t.x+direc[dir].x)] == 1 && dis[(int)(t.y+direc[dir].y)][(int)(t.x+direc[dir].x)] == -1) {
        search.add(new PVector(t.x+direc[dir].x, t.y+direc[dir].y));
        dis[(int)(t.y+direc[dir].y)][(int)(t.x+direc[dir].x)]=d+1;
      }
    }
  }
  println("Task 1: "+task1);
  println("Task 2: "+task2);
}

void search() {
  for(int dir=1;dir<=4;dir++) {
    if(map[(int)(start.y+direc[dir].y)][(int)(start.x+direc[dir].x)]==-1) {
      int res = (int)droid.getResp(dir);
      map[(int)(start.y+direc[dir].y)][(int)(start.x+direc[dir].x)] = res;
      if (res == 2 && goal == null) {
        goal = new PVector((int)start.x+direc[dir].x, (int)start.y+direc[dir].y);
      }
      if (res != 0) {
        start = start.add(direc[dir]);
        search();
        droid.getResp(rev(dir));
        start.add(direc[rev(dir)]);
      }
    }
  }
}

int rev(int d) {
  switch(d) {
    case 1: return 2;
    case 2: return 1;
    case 3: return 4;
    default: return 3;
  }
}

class VM {
  private boolean halted = false;
  private boolean running = false;
  private String s;
  private long index = 0;  //current pos
  private long base = 0;   //for relative mode
  private Map<Long, Long> program;
  private Queue<Long> input = new LinkedList<Long>();
  private Queue<Long> output = new LinkedList<Long>();

  public VM(String input) {
    s = input;
    program = new HashMap<Long, Long>();
    String[] l = s.split(",");
    for (int i=0; i<l.length; i++) {
      program.put((long)i, Long.parseLong(l[i]));
    }
  }

  void input(long i) {
    input.add(i);
    run();
  }

  long getResp(long i) {
    input(i);
    return getLastoutput();
  }

  long getOutput() {
    try {
      return output.remove();
    } 
    catch (Exception e) { 
      return Long.MIN_VALUE;
    }
  }

  long getLastoutput() {
    while (output.size()>2) {
      output.remove();
    }
    return getOutput();
  }

  boolean hasOutput() {
    return output.size()>0;
  }

  void run() {
    if (halted) {
      return;
    }
    running = true;
    while (running) {
      running = doOp(index);
    }
  }

  private boolean doOp(long i) {
    long op = program.get(i);
    long instr = op%100;
    long cf = (op%1000)/100;
    long bf = (op%10000)/1000;
    long af = (op%100000)/10000;

    switch((int)instr) {
    case 1:   //add
      write(i+3, read(i+1, cf)+read(i+2, bf), af);
      index += 4;
      return true;
    case 2:  //mult
      write(i+3, read(i+1, cf)*read(i+2, bf), af);
      index += 4;
      return true;
    case 3:  //input
      if (input.size()>0) {
        write(i+1, input.remove(), cf);
        index += 2;
        return true;
      } else {
        return false;
      }
    case 4:   //output
      prin(program.get(i+1), cf);
      index += 2;
      return true;
    case 5:  //jmpnz
      index = (read(i+1, cf)!=0)? read(i+2, bf):index+3;
      return true;
    case 6:  //jmpeq
      index = (read(i+1, cf)==0)? read(i+2, bf):index+3;
      return true;
    case 7:  //less than
      write(i+3, (read(i+1, cf)<read(i+2, bf))?1:0, af);
      index += 4;
      return true;
    case 8: //equals
      write(i+3, (read(i+1, cf)==read(i+2, bf))?1:0, af);
      index += 4;
      return true;
    case 9: //changing base
      base += read(i+1, cf);
      index += 2;
      return true;
    default:  //halt
      running = false;
      halted = true;
      return false;
    }
  }

  private void prin(long m, long mode) {
    if (mode == 0) {
      output.add(program.get(m));
    } else if (mode == 1) {
      output.add(m);
    } else {
      output.add(program.get(base+m));
    }
  }

  private long read(long pos, long mode) {
    try {
      if (mode == 0) {
        return program.get(program.get(pos));
      } else if (mode == 1) {
        return program.get(pos);
      } else {
        return program.get(base +program.get(pos));
      }
    } 
    catch (NullPointerException e) {
      return 0;
    }
  }

  private void write(long pos, long val, long mode) {
    if (mode == 0) {
      program.put(program.get(pos), val);
    } else {
      program.put(base + program.get(pos), val);
    }
  }
}
