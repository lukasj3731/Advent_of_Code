import java.util.*;

String s = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,35,92,225,1101,25,55,225,1102,47,36,225,1102,17,35,225,1,165,18,224,1001,224,-106,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,68,23,224,101,-91,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,217,13,224,1001,224,-1890,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,69,77,224,1001,224,-5313,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,102,50,22,224,101,-1800,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,89,32,225,1001,26,60,224,1001,224,-95,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,51,79,225,1102,65,30,225,1002,170,86,224,101,-2580,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,39,139,224,1001,224,-128,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,54,93,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226";

String[] l = s.split(",");
int[] program = new int[l.length];
int index = 0;
int input = 1;

void setup() {
  println("Task 1: "+runProg(1));
  println("Task 2: "+runProg(5));
}

int runProg(int in) {
  int ret = 0;
  VM computer = new VM(s);
  computer.input(in);
  while(computer.hasOutput()) {
    ret = (int)computer.getLastoutput();
    computer.input(in);
  }
  return ret;
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
