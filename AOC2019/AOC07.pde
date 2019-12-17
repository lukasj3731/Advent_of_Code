import java.util.*;

String s = "3,8,1001,8,10,8,105,1,0,0,21,38,59,84,97,110,191,272,353,434,99999,3,9,1002,9,2,9,101,4,9,9,1002,9,2,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,5,9,9,101,5,9,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99";
int[][] perm;
String inputs[] = {"01234", "56789"};

void setup() {
  for (int t=0; t<2; t++) {
    int max = 0;
    perm = generatePerms(inputs[t]);
    for (int p=0; p<perm.length; p++) {
      long wire=0;
      VM[] modules = new VM[5];
      for (int i=0; i<modules.length; i++) {
        modules[i] = new VM(s);
        modules[i].run();
        modules[i].input(perm[p][i]);
      }
      int i = 0;
      while (!modules[4].halted) {
        modules[i].input(wire);
        wire = modules[i].getOutput();
        i=(i+1)%5;
      }
      max = max(max, (int)wire);
    }
    println("Task "+(t+1)+": "+max);
  }
}

int[][] generatePerms(String s) {
  String[] m = generatePerms(s, "").split(" ");
  int[][] ret = new int[m.length][m[0].length()];
  for (int i=0; i<m.length; i++) {
    ret[i]=toArr(m[i]);
  }
  return ret;
}

String generatePerms(String str, String ans) {
  if (str.length() == 0) { 
    return ans+" ";
  } 
  String ret = "";
  for (int i = 0; i < str.length(); i++) { 
    char ch = str.charAt(i);
    String ros = str.substring(0, i) + str.substring(i + 1); 
    ret += generatePerms(ros, ans + ch);
  }
  return ret;
}

int[] toArr(String s) {
  int[] ret = new int[s.length()];
  for (int i=0; i<s.length(); i++) {
    ret[i] = Integer.parseInt(""+s.charAt(i));
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
    while (output.size()>1) {
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
