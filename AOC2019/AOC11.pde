import java.util.*;

String in = "3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,2,1105,12,10,1006,0,12,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,58,2,107,7,10,1006,0,38,2,1008,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,90,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,112,1006,0,65,1,1103,1,10,1006,0,91,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,144,1006,0,32,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,169,1,109,12,10,1006,0,96,1006,0,5,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,201,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,223,1,4,9,10,2,8,5,10,1,3,4,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,257,1,1,9,10,1006,0,87,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,287,2,1105,20,10,1,1006,3,10,1,3,4,10,101,1,9,9,1007,9,1002,10,1005,10,15,99,109,641,104,0,104,1,21102,1,932972962600,1,21101,0,336,0,1106,0,440,21101,838483681940,0,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3375393987,0,1,21101,394,0,0,1105,1,440,21102,46174071847,1,1,21102,1,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,988648461076,0,1,21101,428,0,0,1106,0,440,21101,0,709580452200,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,471,3,21102,461,1,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,0,1,466,109,-2,2105,1,0,0,109,4,1202,-1,1,503,1207,-3,0,10,1006,10,521,21102,1,0,-3,22102,1,-3,1,21201,-2,0,2,21101,0,1,3,21102,540,1,0,1106,0,545,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22101,0,-4,-4,1105,1,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,587,0,1105,1,545,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,606,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,21201,-1,0,1,21101,0,628,0,106,0,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0";
String[] l = in.split(",");
int[] list = new int[l.length];

PVector pos = new PVector(200,200);
PVector dir = new PVector(0,1);
int[][] ship = new int [400][400];

void setup() {
  size(400,400);
  background(0);
  for(int i=0;i<ship.length;i++) {
    for(int j=0;j<ship[i].length;j++) {
      ship[i][j] = -1;
    }
  }
  
  VM brain = new VM(in);
  brain.run();
  
  while(!brain.halted) {
    brain.input(ship(pos.x,pos.y));
    long c = brain.getOutput();
    long d = brain.getOutput();
    ship[(int)pos.x][(int)pos.y] = (int)c;
    dir.rotate((d==0)?PI/2.0:-PI/2.0);
    pos = pos.add(dir);
  }
  
  int counter = 0;
  for(int i=0;i<ship.length;i++) {
    for(int j=0;j<ship[i].length;j++) {
      if(ship[i][j] != -1) {
        counter++;
      }
    }
  }
  println(counter);
  
  for(int i=0;i<ship.length;i++) {
    for(int j=0;j<ship[i].length;j++) {
      ship[i][j] = -1;
    }
  }
  ship[(int)pos.x][(int)pos.y]=1 ;
  
  brain = new VM(in);
  brain.run();
  
  while(!brain.halted) {
    brain.input(ship(pos.x,pos.y));
    long c = brain.getOutput();
    long d = brain.getOutput();
    ship[(int)pos.x][(int)pos.y] = (int)c;
    dir.rotate((d==0)?PI/2.0:-PI/2.0);
    pos = pos.add(dir);
  }
  for(int i=0;i<ship.length;i++) {
    for(int j=0;j<ship[i].length;j++) {
      if(ship[j][i] == 1) {
        set(ship.length-i,ship[i].length-j,color(255));
      }
    }
  }
}


int ship(float x, float y) {
  int m = ship[(int)x][(int)y];
  if(m==-1) {
    return 0;
  }
  return m;
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
