String s = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0";
String[] l = s.split(",");
int[] program = new int[l.length];

void setup() {
  println("Task 1: "+runProg(12,2));
  for(int n = 0;n<100;n++) {
    for(int v = 0;v<100;v++) {
      if(runProg(n,v)==19690720) {
        println ("Task 2: "+(100*n+v));
      }
    }
  }
}

int runProg(int noun, int verb) {
  for(int i=0;i<l.length;i++) {
    program[i] = Integer.parseInt(l[i]);
  }
  program[1] = noun;
  program[2] = verb;
  
  boolean running = true;
  int index = 0;
  
  while(running) {
    running = doOp(index);
    index += 4;
  }
  return program[0];
}

boolean doOp(int index) {
  int op = program[index];
  if(op == 99) {
    return false;
  } else {
    int a = program[program[index+1]];
    int b = program[program[index+2]];
    if(op == 1) {
      program[program[index+3]] = a+b;
    } else {
      program[program[index+3]] = a*b;
    }
    return true;
  }
}
