import java.util.*;

String s = "109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1106,0,259,1202,1,1,221,203,1,21101,0,31,0,1105,1,282,21102,38,1,0,1105,1,259,20102,1,23,2,21201,1,0,3,21102,1,1,1,21101,0,57,0,1105,1,303,2101,0,1,222,20102,1,221,3,21002,221,1,2,21101,0,259,1,21101,0,80,0,1106,0,225,21102,1,152,2,21101,91,0,0,1106,0,303,1201,1,0,223,21001,222,0,4,21101,0,259,3,21102,225,1,2,21101,0,225,1,21102,1,118,0,1105,1,225,20101,0,222,3,21102,61,1,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1105,1,259,2101,0,1,223,21001,221,0,4,21001,222,0,3,21101,0,14,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,21202,-3,1,1,21202,-2,1,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21101,0,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2106,0,0";

VM drone = new VM(s);

int shipSize = 2000;
void setup() {
  println("Task 1: "+countSpaces(50)+"");
  println("Task 2: "+fitShip(100)+"");
}

int countSpaces(int len) {
  int sum =0;
  for (int i=0; i<len; i++) {
    for(int j=0;j<len;j++) {
      if(Pos(i,j)) sum++;
    }
  }
  return sum;
}

int fitShip(int size) {
  int x = 100, y = 0;
  while (true) {
    if (Pos(x, y)) {
      if (Pos(x-(size-1), y+(size-1))) {
        return 10000 * (x - (size-1)) + y;
      } else {
        x++;
      }
    } else {
      y++;
    }
  }
}

boolean Pos(int x, int y) {
  drone.reset();
  drone.input(x);
  drone.input(y);
  return drone.getLastoutput()==1;
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

  void reset() {
    program = new HashMap<Long, Long>();
    String[] l = s.split(",");
    for (int i=0; i<l.length; i++) {
      program.put((long)i, Long.parseLong(l[i]));
    }
    index = 0;
    base = 0;
    halted = false;
    running = false;
  }
}
